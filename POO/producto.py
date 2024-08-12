class Producto:
    def __init__(self,nombre,precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    def mostrar(self):
        return f"El producto es: {self.nombre} \nPrecio:{self.precio},\ncantidad: {self.cantidad}"

    def agregar_stock(self,cantidad):
        self.cantidad += cantidad
        print(f"Se han agregado: {cantidad} unidades de {self.nombre}, la cantida actual es: {self.cantidad}")
    
    def vender(self,cantidad):
        if cantidad > self.cantidad:
            print(f" No hay suficiente stock de {self.nombre}, solo hay {self.cantidad}")
        else:
            self.cantidad -= cantidad 
            print(f"Se ha Vendido{cantidad} del producto {self.nombre}, Y queda en  stock:{self.cantidad}") 
            
#Main
#agrega inputs
nombre_pr1=input("Ingresa el producto 1")
precio_pr1=int(input("Ingresa el precios del producto 1"))
cantidad_pr1=int(input("Ingresa la cantidad producto1"))

producto1= Producto(nombre_pr1, precio_pr1, cantidad_pr1) 
producto2= Producto("Mesa", 200, 30)      
#Mostra los  datos productos
print(producto1.mostrar())
print(producto2.mostrar())
#Agregamos 10 y mostramos el producto de la laptop
cantidaAgregar=int(input("Producto deseas agregar"))
producto1.agregar_stock(cantidaAgregar) 
print(producto1.mostrar())  
#Vender 15 unidades y mostrar  el producto2
producto2.vender(15) 
print(producto2.mostrar()) 
#Vender 40 unidades y mostrar  el producto1
producto1.vender(40) 
print(producto1.mostrar())        