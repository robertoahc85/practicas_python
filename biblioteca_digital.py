"""Memoria actualizada
Proyecto Práctico en Python: "Gestión de una Biblioteca Digital"
Descripción:
En este proyecto, los alumnos desarrollarán un programa para gestionar una biblioteca digital. El programa permitirá agregar, buscar, y listar libros. Además, contará con funcionalidades para llevar un registro de los libros prestados y devueltos. El proyecto integrará varios conceptos clave como if, for, while, funciones, estructuras de datos (listas y diccionarios), sentencias condicionales, control de flujo y operadores lógicos.
Objetivos:
Aplicar estructuras de control de flujo (if, for, while).
Definir y utilizar funciones.
Manipular estructuras de datos como listas y diccionarios.
Implementar operadores lógicos para la toma de decisiones.
Instrucciones:
Crear el Menú Principal:
El programa debe mostrar un menú con las siguientes opciones:
Agregar un libro.
Buscar un libro.
Listar todos los libros.
Registrar un préstamo.
Registrar una devolución.
Salir.
Agregar un Libro:
Solicitar al usuario ingresar el título del libro, autor, y el año de publicación.
Almacenar la información en una lista de diccionarios.
Cada libro debe ser representado como un diccionario con las claves: titulo, autor, año, y prestado (inicialmente  False).
Buscar un Libro:
Permitir buscar un libro por título.
Utilizar un bucle for para recorrer la lista de libros y encontrar coincidencias.
Mostrar los detalles del libro si se encuentra, o un mensaje indicando que no existe.
Listar Todos los Libros:
Recorrer la lista de libros utilizando un bucle for.
Mostrar el título, autor, año de publicación y si está prestado o disponible.
Registrar un Préstamo:
Solicitar el título del libro que se desea prestar.
Verificar si el libro está disponible (prestado == False).
Si está disponible, marcarlo como prestado (prestado = True).
Si no está disponible, mostrar un mensaje indicando que ya está prestado.
Registrar una Devolución:
Solicitar el título del libro que se desea devolver.
Verificar si el libro está prestado (prestado == True).
Si está prestado, marcarlo como disponible (prestado = False).
Si no está prestado, mostrar un mensaje indicando que no se encontraba prestado.
Salir:
Terminar la ejecución del programa cuando el usuario selecciona la opción de salida.
Extensiones Sugeridas:
Agregar un sistema de usuarios: Crear una lista de usuarios que puedan prestar libros.
Implementar un límite de préstamos: Establecer un máximo de libros que un usuario puede prestar a la vez.
Historial de préstamos: Registrar y mostrar un historial de los libros prestados y devueltos por cada usuario."""

# Estructura principal
libros = []

def mostrar_menu():
    print("\n--- Menú Biblioteca Digital ---")
    print("1. Agregar un libro")
    print("2. Buscar un libro")
    print("3. Listar todos los libros")
    print("4. Registrar un préstamo")
    print("5. Registrar una devolución")
    print("6. Salir")

def agregar_libro():
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    año = input("Ingrese el año de publicación: ")
    libro = {"titulo": titulo, "autor": autor, "año": año, "prestado": False}
    libros.append(libro)
    print(f"Libro '{titulo}' agregado correctamente.")

def buscar_libro():
    titulo = input("Ingrese el título del libro que busca: ")
    for libro in libros:
        if libro["titulo"].lower() == titulo.lower():
            print(f"Encontrado: {libro}")
            return
    print("Libro no encontrado.")

def listar_libros():
    if not libros:
        print("No hay libros en la biblioteca.")
    else:
        for libro in libros:
            estado = "Prestado" if libro["prestado"] else "Disponible"
            print(f"Título: {libro['titulo']}, Autor: {libro['autor']}, Año: {libro['año']}, Estado: {estado}")

def registrar_prestamo():
    titulo = input("Ingrese el título del libro a prestar: ")
    for libro in libros:
        if libro["titulo"].lower() == titulo.lower():
            if not libro["prestado"]:
                libro["prestado"] = True
                print(f"Libro '{titulo}' prestado exitosamente.")
            else:
                print(f"El libro '{titulo}' ya está prestado.")
            return
    print("Libro no encontrado.")

def registrar_devolucion():
    titulo = input("Ingrese el título del libro a devolver: ")
    for libro in libros:
        if libro["titulo"].lower() == titulo.lower():
            if libro["prestado"]:
                libro["prestado"] = False
                print(f"Libro '{titulo}' devuelto exitosamente.")
            else:
                print(f"El libro '{titulo}' no estaba prestado.")
            return
    print("Libro no encontrado.")

def ejecutar_programa():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_libro()
        elif opcion == "2":
            buscar_libro()
        elif opcion == "3":
            listar_libros()
        elif opcion == "4":
            registrar_prestamo()
        elif opcion == "5":
            registrar_devolucion()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

# Ejecutar el programa
ejecutar_programa()
