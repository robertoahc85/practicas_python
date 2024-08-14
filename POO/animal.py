class Animal:
    def __init__(self,patas):
        self.patas = 4
   
    def hacer_sonido(self):
        return "Grrr!"
    def comer(self):
        return "Esta comiendo"
    
class Perro(Animal):  
    def __init__(self,patas):
      super().__init__(patas)
      
    def hacer_sonido(self):
        return "Gua!"
class Canguro(Animal): 
      def __init__(self,patas):
            self.patas = 2
      
class Gato(Animal):
    def hacer_sonido(self):
        return "Miau!Miau!"
    def salta(self):
        return "Salta muy alto"
         
class Vaca(Animal):
    def hacer_sonido(self):
        return "Muu!" 
    def comer(self):
        return "Comiendo Pasto"
       
def animal_sonido(animal):
    print(animal.hacer_sonido())
def animal_comiendo(animal):
    print(animal.comer())   
    
perro =Perro(4) 
gato = Gato(4) 
vaca = Vaca(4)
canguro=Canguro(4)

print(gato.salta())
print(perro.patas)
print(canguro.patas)
# print(perro.name)
# animal_sonido(perro)
# animal_sonido(gato)
# animal_sonido(vaca)
animales = [Perro(4),Gato(4),Vaca(4),Perro(4),Vaca(4)]
for animal in animales:
    animal_sonido(animal)
    animal_comiendo(animal)

             