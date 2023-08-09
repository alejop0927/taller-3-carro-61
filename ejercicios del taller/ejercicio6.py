class Carta:
    # Constantes para las pintas de la carta
    CORAZON = "Corazón"
    DIAMANTE = "Diamante"
    TREBOL = "Trébol"
    ESPADA = "Espada"

    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

# Crear instancias de la clase Carta con diferentes valores y pintas
carta1 = Carta("As", Carta.CORAZON)
carta2 = Carta("Rey", Carta.DIAMANTE)
carta3 = Carta("10", Carta.TREBOL)
carta4 = Carta("7", Carta.ESPADA)

# Imprimir los atributos de las cartas creadas
print(f"Carta 1: Valor - {carta1.valor}, Pinta - {carta1.pinta}")
print(f"Carta 2: Valor - {carta2.valor}, Pinta - {carta2.pinta}")
print(f"Carta 3: Valor - {carta3.valor}, Pinta - {carta3.pinta}")
print(f"Carta 4: Valor - {carta4.valor}, Pinta - {carta4.pinta}")