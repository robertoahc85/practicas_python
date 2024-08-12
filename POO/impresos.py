# Clase libro
class Book:
#pass # para declara que una clase no haga nada
    def __init__(self,title,author):
        self.title=title
        self.author=author
        
#clase Periodico
class Newspaper:
    def __init__(self,title):
        self.title=title 
#Main
#creando objetos
book1= Book("100 anios de soledad","Gabriel Garcia Marquez")
book2= Book("Codigo Limpio","Robert C. Martin")
periodico=Newspaper("El Universal")
periodico2=Newspaper("Times")

#invocando objetos de clase book
print(book1)
print(book2)
print(book2.title)
print(book1.author)
print(book2.author)
#invocando objeto de la clase Newspaper
print(periodico.title)
print(periodico2.title)