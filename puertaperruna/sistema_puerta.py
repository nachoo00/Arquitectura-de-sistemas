import threading
import time
from sensores import Sensores
from actor_puerta import ActuadorPuerta

class SistemaPuerta:
    def __init__(self):
        self.sensores = Sensores()
        self.actuador = ActuadorPuerta()

    def procesar_ladrido(self, sonido):
        if self.sensores.detectar_ladrido(sonido):
            self.actuador.abrir()
            self._iniciar_cierre_automatico()

    def _iniciar_cierre_automatico(self):
        def cierre_automatico():
            time.sleep(5)  # Esperar antes de cerrar
            while not self.sensores.es_seguro_cerrar():
                time.sleep(1)  # Revisar cada segundo
            self.actuador.cerrar()

        threading.Thread(target=cierre_automatico).start()

# Prueba rápida
if __name__ == "__main__":
    sistema = SistemaPuerta()
    sistema.procesar_ladrido("Guau Guau")
