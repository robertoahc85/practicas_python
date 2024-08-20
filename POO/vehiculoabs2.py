#hacer clase vehiculo que tenga los metodos moverse y describirse
    #clase hija, moto, auto, bicicleta
    # todas las clase hija debe tener metodo propio
from abc import ABC,abstractmethod

# Clase Coche
class Vehiculo(ABC):
    def __init__(self, marca, modelo,anio):
        self.marca=marca
        self.modelo=modelo
        self.anio= anio
    @abstractmethod
    def describirse(self):
        pass
    @abstractmethod
    def moverse(self):
        pass
#clase moto    
class Moto(Vehiculo):
    def describirse(self): 
        return f"Coche: {self.marca} ,\nModeloe{self.modelo},\nanio:{self.anio}"
    def encender(self):
        return f"La moto es: {self.marca},{self.modelo} esta arrancando"
    def hacer_ruido(self):
        return f"La moto: {self.marca},{self.modelo} esta haciendo ruido"
    def moverse(self):
        return f"La moto: {self.marca},{self.modelo} prendio la radio"
    
class Auto(Vehiculo):
    def describirse(self):
        return f"Coche: {self.marca} ,\nModeloe{self.modelo},\nanio:{self.anio}"
    def encender(self):
        return f"El auto es: {self.marca},{self.modelo} esta arrancando"
    def prender_radio(self):
        return f"La moto: {self.marca},{self.modelo} prendio la radio"
    def moverse(self):
        return f"La moto: {self.marca},{self.modelo} prendio la radio"

class Bicicleta(Vehiculo):
    def describirse(self):
        return f"Coche: {self.marca} ,\nModeloe{self.modelo},\nanio:{self.anio}"
    def enceder(self):
        return f"La bicicleta es: {self.marca},{self.modelo} esta arrancando"
    def pedalear(self):
        return f"La bicicleta {self.marca},{self.modelo} esta pedaleando"
    def moverse(self):
        return f"La moto: {self.marca},{self.modelo} prendio la radio"

#Main 
#invocar las clase coche   
mi_coche =Auto("Toyota","Yaris","2017")#Crear objeto coche
print(mi_coche.describirse())
print(mi_coche.moverse())
print(mi_coche.prender_radio())

mi_moto = Moto("Yamaha","XR","2020")
mi_moto2 = Moto("Ducatti","Multiestraba","2023")
print(mi_moto.describirse())
print(mi_moto.moverse())
print(mi_moto.hacer_ruido())

mi_bicicleta = Bicicleta("Bicicleta","Bicicleta","2014")
print(mi_bicicleta.describirse())
print(mi_bicicleta.moverse())
print(mi_bicicleta.pedalear())