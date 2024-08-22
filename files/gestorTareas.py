class GestorTareas:
    def __init__(self,archivo_tareas="tareas.txt"):
        self.archivo_tareas = archivo_tareas
    def abrir_archivo(self,archivo):
        pass    
    def anadir_tareas(self,tarea):
        with  open( self.archivo_tareas,'a') as archivo:
            archivo.write(tarea + '\n')
        print("Tarea agregada con exito") 
    def mostrar_tareas(self):
        pass
    def contar_tareas(self):
        pass
    def buscar_remplazar(self,palabra_buscar,palabra_remplazar):
        pass
    def hacer_respaldo(self):
        pass
 #Completar los menus, agregar excepcion        
             
 
def main():
    gestor = GestorTareas()
    while True:
        print("\n--------Menu-----------")
        print("1.Anadir Tarea")
        print("2.Mostrar Tarea")
        print("3.Contar numero de Tareas")
        print("4 .Buscar y remplanzar")
        print("5 .Hacer Respaldo")
        print("6.Salir")
        opcion = int(input("Elige una opcion: "))
        if (opcion == 1):
            tarea = input("Ingresa una nueva tarea")
            gestor.anadir_tareas(tarea)
        elif (opcion == 6):
            print("Saliendo del programa")
            break
        else:
            print("opcion no valida")    

if __name__ == '__main__':
    main()   
    /Users/roberto.hernanderz/Documents/Eductecno/Phyton 2024/Practicas /python-Modulo3-4/practicas_python/files                 