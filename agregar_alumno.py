# Crea un programa en Python que gestione la información de los estudiantes de una escuela. 
# El programa debe permitir 
    # agregar nuevos estudiantes,
    # mostrar la lista de estudiantes 
    #buscar un estudiante por su nombre.
    
# Requisitos
# Funciones:
# agregar_estudiante(nombre, edad, grado): Agrega un nuevo estudiante a la lista.
# mostrar_estudiantes(): Muestra la lista completa de estudiantes.
# buscar_estudiante(nombre): Busca un estudiante por su nombre y muestra su información.

# Interacción con el Usuario:
# El programa debe mostrar un menú con las opciones:
    # "Agregar estudiante",
    # "Mostrar estudiantes", 
    # "Buscar estudiante" y
    # "Salir".
    
# La opción "Agregar estudiante" 
    #   debe pedir el nombre,
    #   edad 
    #    grado del estudiante.

# La opción "Mostrar estudiantes" 
#   debe mostrar la lista completa de estudiantes.
# La opción "Buscar estudiante" 
#   debe pedir el nombre del estudiante y mostrar su información si se encuentra en la lista.

#Metodos
estudiantes=[]

def agregar_estudiante(nombre, edad, grado):
    estudiante ={"nombre":nombre, "edad":edad, "grado":grado}
    estudiantes.append(estudiante)
    
def mostrar_estudiantes():
    if not estudiantes:
        print("No hay estudiantes inscritos")
    else:
        for estudiante in estudiantes:
            print(f"El Nombre del estudiante es: {estudiante['nombre']},su edad es: {estudiante['edad']}, y su grados es:{estudiante['grado']} ")  

def buscar_estudiante(nombre):
    for estudiante in estudiantes:
        if estudiante['nombre'].lower() == nombre.lower():
            print(f"Estudiante encontrado sus datos son:\nNombre: {estudiante['nombre']},edad:{estudiante['edad']},el grado:{estudiante['grado']}")
            break
    else:
        print("Estudiante no encontrado")

def mostrar_menu():
    print("***Bienvenido al Gestion de Estudiantes 0077*****")  
    print("Seleccion una opcion:") 
    print("1. Agregar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Buscar estudiante")
    print("4. Salir")
    
def  pedir_info_alumno():
    nombre=input("Dame el Nombre del alumno")
    edad=int(input("Dame la edad del alumno"))
    grado=input("Dame el grado del alumnos")
    return nombre,edad,grado
def validar_opcion(opcion):
    
    return opcion

def admon_estudiantes():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Ingrese la opcion deseada: "))
            
            if opcion == 1:
                nombre, edad, grado = pedir_info_alumno()
                agregar_estudiante(nombre, edad, grado)
            elif opcion == 2:
                mostrar_estudiantes()
            elif opcion == 3:
                nombre = input("Ingresa el nombre del alumno a buscar: ")
                buscar_estudiante(nombre)
            elif opcion == 4:
                print("Gracias por usar sistemas 0077")
                break     
            else:
                print("Opción no válida")
        
        except ValueError:
            print("Error: Por favor, ingresa un número válido para la opción.")     


#Main
admon_estudiantes()



