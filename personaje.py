import random

class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0

    @property
    def estado(self):
        return (
            f"Nombre: {self.nombre}",
            f"Nivel {self.nivel}",
            f"Experiencia: {self.experiencia}",
        )

    def probabilidad_ganar(self, other):
        diferencia_niveles = self.nivel - other.nivel

        if diferencia_niveles > 0:
            return min(1.0, 0.33 + 0.1 * diferencia_niveles)
        elif diferencia_niveles < 0:
            return max(0.0, 0.5 - 0.1 * abs(diferencia_niveles))
        else:
            return 0.5

    @staticmethod
    def mostrar_dialogo_opcion(probabilidad_ganar):
        return int(
            input(
                f"\nCon tu nivel actual, tienes {probabilidad_ganar * 100}% "
                "de probabilidades de ganarle al Orco.\n"
                "\nSi ganas, ganarás 50 puntos de experiencia y el orco perderá 30. \n"
                "Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.\n"
                "\n¿Qué deseas hacer?\n"
                "1. Atacar\n"
                "2. Huir\n"
            )
        )

    def enfrentar_orco(self, orco):
        probabilidad_ganar = self.probabilidad_ganar(orco)
        opcion = self.mostrar_dialogo_opcion(probabilidad_ganar)

        while opcion == 1:
            resultado_ataque = "Gana" if random.uniform(0, 1) <= probabilidad_ganar else "Pierde"

            if resultado_ataque == "Gana":
                self.experiencia += 50
                orco.experiencia -= 30
            else:
                self.experiencia -= 30
                orco.experiencia += 50

            print("\nResultado del ataque:", resultado_ataque)
            print("Estado actualizado del Orco:")
            print("\n".join(orco.estado))
            print("Estado actualizado de tu personaje:")
            print("\n".join(self.estado))

            probabilidad_ganar = self.probabilidad_ganar(orco)
            opcion = self.mostrar_dialogo_opcion(probabilidad_ganar)

        print("\nHas decidido huir. El orco ha quedado atrás.")
