import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def calcular_area(self):
        area = math.pi * self.radio ** 2
        return area

    def calcular_perimetro(self):
        perimetro = 2 * math.pi * self.radio
        return perimetro

    def punto_pertenece(self, punto):
        distancia_al_centro = math.sqrt((punto.x - self.centro.x)**2 + (punto.y - self.centro.y)**2)
        return distancia_al_centro <= self.radio

# Crear un punto para el centro del círculo
centro = Punto(0, 0)

# Crear una instancia de la clase Circulo
circulo = Circulo(centro, 5)

# Calcular y mostrar el área y el perímetro del círculo
print("Área del círculo:", circulo.calcular_area())
print("Perímetro del círculo:", circulo.calcular_perimetro())

# Verificar si un punto pertenece al círculo
punto_prueba = Punto(3, 4)
if circulo.punto_pertenece(punto_prueba):
    print("El punto pertenece al círculo.")
else:
    print("El punto no pertenece al círculo.")
