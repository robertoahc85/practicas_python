#clases
class Dog:
    def __init__(self, name,raza):
        self.name = name
        self.raza = raza
        
    def ladrar(self):
          print(f"El perro {self.name},ladra asi WuaWua, y es de raza {self.raza}")
          
#Principal o Main  
perro =Dog("Jefazo","labrador") 
perro.ladrar() # mandamos traer un metodo de un clase
    