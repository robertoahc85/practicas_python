#sobrescribiendo archivo txt
with open('files/ejemplo.txt',"w") as archivo:
    archivo.write("Hola Desde Tlaxcala Mexico\n")
    archivo.write("Esta es una linea nueva\n")
    archivo.write("Aqui estuvo Ivan\n")
    archivo.write("Ya son casi la Vacaciones")
    
#leer archivo    
with open("files/ejemplo.txt","r")  as lectura:
    contenido= lectura.read()
    print(contenido)   
 
#Anadir contenido al final del archivo    
with open("files/ejemplo.txt","a") as  f:
    f.write("Esta es una linea la estamos agregando al final") 
    
#leer archivo    
with open("files/ejemplo.txt","r")  as lectura:
    contenido= lectura.read()
    print(contenido)         

# Manejos de errores
with open("files/ejemplo2.txt","r") as file:
    try:
        contenido= file.read()
        print(contenido)
    except FileNotFoundError:
        print("No se encuentra el archivo")
        
with open("files/ejemplo.txt","r") as  archivo:
    contador= 0
    for linea in archivo:
        contador += 1
        print(f"El archivo tiene: {linea.strip()} lineas")   
    print(f"El total de linez es {contador}")
    