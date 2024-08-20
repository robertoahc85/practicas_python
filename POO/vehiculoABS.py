#hacer clase vehiculo que tenga los metodos moverse y describirse
    #clase hija, moto, auto, bicicleta
    # todas las clase hija deber un metodo propio
#usado abstracion y herencia
   
    
from abc import ABC, abstractmethod

# Clase base abstracta
class Vehiculo(ABC):
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    @abstractmethod
    def describir(self):
        pass
    
    @abstractmethod
    def arrancar(self):
        pass

# Clase Coche que hereda de Vehiculo
class Coche(Vehiculo):
    def describir(self):
        return f"Coche: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}"

    def arrancar(self):
        return f"El coche {self.marca} {self.modelo} está arrancando"

# Clase Moto que hereda de Vehiculo
class Moto(Vehiculo):
    def describir(self):
        return f"Moto: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}"

    def arrancar(self):
        return f"La moto {self.marca} {self.modelo} está arrancando"

# Main
# Crear objeto Coche
mi_coche = Coche("Toyota", "Yaris", "2017")
print(mi_coche.describir())
print(mi_coche.arrancar())

# Crear objetos Moto
mi_moto = Moto("Yamaha", "XR", "2020")
mi_moto2 = Moto("Ducati", "Multistrada", "2023")
print(mi_moto.describir())
print(mi_moto2.describir())
