#importar clase Personaje 
from personaje import Personaje

# define la clase Juego
class Juego:
    
    # Constructor __init__
    def __init__(self):
        
        # mensaje de bienvenida 
        print("¡Bienvenido al juego!")
        
        # solicita nombre persona
        nombre_jugador = input("Ingresa el nombre para tu personaje: ")
        self.jugador = Personaje(nombre_jugador)
        
        # muestra inicio
        print("\nEstado de tu personaje:")
        print("\n".join(self.jugador.estado))

        self.orco = Personaje("Orco")
        print("Ha aparecido un Orco.")
        
        # probabilidad
        probabilidad_ganar = self.jugador.probabilidad_ganar(self.orco)
        print(f"Probabilidad de ganar al Orco: {probabilidad_ganar * 100}%")

        #enfrentamiento 
        self.jugador.enfrentar_orco(self.orco)

if __name__ == "__main__":
    juego = Juego()
