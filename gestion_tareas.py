# Simulador de Gestión de Tareas Personales"
# Descripción:
# En este proyecto, los alumnos desarrollarán un simulador de gestión de tareas personales. El programa permitirá a los usuarios agregar, eliminar, marcar como completadas, y listar tareas pendientes. El proyecto integrará conceptos clave como if, for, while, funciones, estructuras de datos (listas y diccionarios), sentencias condicionales, control de flujo, y operadores lógicos.
# Objetivos:
# •	Utilizar estructuras de control de flujo (if, for, while).
# •	Definir y organizar el código en funciones.
# •	Manipular listas y diccionarios para almacenar y gestionar datos.
# •	Aplicar operadores lógicos en la toma de decisiones.
# Instrucciones:
# 1.	Crear el Menú Principal:
# El programa debe mostrar un menú con las siguientes opciones:
# 1.	Agregar una tarea.
# 2.	Marcar una tarea como completada.
# 3.	Eliminar una tarea.
# 4.	Listar todas las tareas.
# 5.	Salir.
# 2.	Agregar una Tarea:
# o	Solicitar al usuario ingresar la descripción de la tarea y la fecha de vencimiento.
# o	Almacenar la tarea en una lista como un diccionario con las claves: descripcion, fecha, y completada (inicialmente False).
# 3.	Marcar una Tarea como Completada:
# o	Permitir al usuario seleccionar una tarea de la lista para marcarla como completada (completada = True).
# o	Usar un bucle for para encontrar la tarea en la lista.
# 4.	Eliminar una Tarea:
# o	Permitir al usuario seleccionar una tarea para eliminarla de la lista.
# o	Verificar si la tarea existe y, de ser así, eliminarla de la lista.
# 5.	Listar Todas las Tareas:
# o	Recorrer la lista de tareas utilizando un bucle for.
# o	Mostrar la descripción, fecha de vencimiento y estado (completada o pendiente) de cada tarea.
# 6.	Salir:
# o	Terminar la ejecución del programa cuando el usuario selecciona la opción de salida

tareas=[]
def agregar_tarea():
    descripcion=input("Ingresa la descripcion de la tarea:")
    fecha= input("Ingresa la fecha de vencimiento(dd/mm/aaaa)")
    tarea= {"descripcion":descripcion, "fecha":fecha,"completada":False}
    tareas.append(tarea)
    print(f"Tarea  de: {descripcion} agregada con exito")
    
def marcarCompletada():
    descripcion=input("ingresa la descripcion de la tarea a marca completada") 
    for tarea in tareas:
        if tarea['descripcion'].lower() == descripcion.lower():  
            if not tarea['completada']:
                tarea['completada'] =True
                print(f"Tarea marcada como Completada exitosamente")
            else:
                print(f"La tarea {descripcion} la tarea ya estaba completada") 
    print("La tarea no encontrada")               

def eliminar_tarea():
    descripcion=input("ingresa la descripcion de la tarea a marca completada") 
    for tarea in tareas:
        if tarea['descripcion'].lower() == descripcion.lower():
            tareas.remove(tarea) 
            print(f"Tarea eliminada con exito") 
print("La tarea no encontrada")   

def listar_tareas():
    if not tareas:
        print("No hay tareas en la lista")
    else:
        for tarea in tareas:
            print(f"--Descripcion:{tarea['descripcion']}, fecha:{tarea['fecha']}, Completada:{tarea['completada']}")
             
def mostrar_menu():
    print("-------Menu de Gestion de Tareas--------")
    print("1.Agregar una tarea")
    print("2.Marcar tarea como completada")
    print("3.Eliminar tarea")
    print("4.listar tareaas")
    print("5.Salir")
    
def ejecutar_programa(): 
    while True:
        mostrar_menu()   
        opcion=int(input("Selecione una opcion:"))
        if opcion== 1:
            agregar_tarea()
        elif  opcion== 2:
            marcarCompletada()
        elif opcion== 3:
            eliminar_tarea() 
        elif opcion== 4:
            listar_tareas()  
        elif opcion== 5:
            print("Gracias por usar nuestro sistema, hasta luego")  
            break
        else:        
         print("opcion no valida") 
            
#Main   
ejecutar_programa()                      