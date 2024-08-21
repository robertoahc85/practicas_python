class GestorTareas:
    def __init__(self,archivo_tareas="tareas.txt"):
        self.archivo_tareas = archivo_tareas
        
    def anadir_tareas(self,tarea):
        with  open( self.archivo_tareas,'a') as archivo:
            archivo.write(tarea + '\n')
        print("Tarea agregada con exito")    
 
def main():
    gestor = GestorTareas()
    while True:
        print("\n--------Menu-----------")
        print("1.Anadir Tarea")
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