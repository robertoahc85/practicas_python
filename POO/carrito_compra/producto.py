#Excepcionada Personalizada
class StockInsuficienteError(Exception):
    pass

class Producto:
    def __init__(self,nombre,precio, cantidad_stock):
        self.__nombre = nombre #Atributo privado
        self.__precio = precio #Atributo privado
        self.__cantidad_stock = cantidad_stock #Atributo privado
    #Get usando propiedades    
    @property
    def nombre(self):
        return self.__nombre
    @property
    def precio(self):
        return self.__precio
    @property
    def cantidad_stock(self):
        return self.__cantidad_stock
    #Set usando propiedades
    @precio.setter
    def precio(self,valor):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo")
        self.__precio = valor
        
    @cantidad_stock.setter
    def cantidad_stock(self,cantidad):  
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        self.__cantidad_stock =cantidad
    def reducir_stock(self,cantidad):
        if cantidad > self.__cantidad_stock:
            raise StockInsuficienteError("Stock insuficiente para la cantidad solicitada")
        self.__cantidad_stock -= cantidad    