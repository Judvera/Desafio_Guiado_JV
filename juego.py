from personaje import Personaje

class Juego:
    def __init__(self):
        print("¡Bienvenido al juego!")
        nombre_jugador = input("Ingresa el nombre para tu personaje: ")
        self.jugador = Personaje(nombre_jugador)
        print("\nEstado de tu personaje:")
        print("\n".join(self.jugador.estado))

        self.orco = Personaje("Orco")
        print("Ha aparecido un Orco.")
        probabilidad_ganar = self.jugador.probabilidad_ganar(self.orco)
        print(f"Probabilidad de ganar al Orco: {probabilidad_ganar * 100}%")

        self.jugador.enfrentar_orco(self.orco)

if __name__ == "__main__":
    juego = Juego()
