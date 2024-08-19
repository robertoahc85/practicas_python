from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    def eat(self):
        pass
    
class Dog(Animal):
    def sound(self):
        return "guagua" 
    def eat(self):
        return "Comiendo croquetas"

class Cat(Animal):
    def sound(self):
        return "Miau" 

class Pink(Animal):
    def comer(self):
        return "comiendo"
        
#Main
perro = Dog()
gato =  Cat()

print (gato.sound())
print (perro.sound())     
oink = Pink()     