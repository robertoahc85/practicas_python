#ducktyping
class Pato:
    def volar(self):
        print("El pato Vuela")
    def nadar(self):
        print("El pato nada")    

class Persona:
    def volar(self):
        print("La persona Vuela en Avion")
    def nadar(self):
        print("La persona nada en la piscina") 
        
class Pez:
    def volar(self):
        print("El pez Vuela mientra salta")
    def nadar(self):
        print("El pez nada en el mar")        

def hacer_volar_y_nada(objecto):
    objecto.volar()
    objecto.nadar()
    
lucas = Pato()
roberto = Persona()
nemo = Pez()

hacer_volar_y_nada(lucas)
hacer_volar_y_nada(roberto)
hacer_volar_y_nada(nemo)
               