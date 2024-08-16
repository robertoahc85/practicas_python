class Figura:
    def __init__(self, lados, longitud):
        self.lados = lados
        self.longitud = longitud

    def calcular_perimetro(self):
        return self.lados * self.longitud

class Poligono(Figura):
    def __init__(self, lados, longitud):
        super().__init__(lados, longitud)

# Ejemplo de uso
cuadrado = Poligono(4, 5)
pentagono = Poligono(5, 5)
exagono = Poligono(6, 5)
octagono = Poligono(8, 5)

print(cuadrado.calcular_perimetro())  # Output: 20
print(pentagono.calcular_perimetro()) # Output: 25
print(exagono.calcular_perimetro())   # Output: 30
print(octagono.calcular_perimetro())  # Output: 40

