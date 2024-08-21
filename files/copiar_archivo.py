#copiar el contenido de un archivo a otro
def copiar_archivo(archivo_origen,archivo_destino):
    try:
        #Abrimos el archivo origen en modo lectura
        with open(archivo_origen,"r") as origen:
            contenido = origen.read() #leemos el cotenido origen
        #abrir el archivo destino en modo de escritura
        with open(archivo_destino,"w") as destino:
            destino.write(contenido)  #Escribir el contenido en el nuevo archivo  
    except FileNotFoundError:
        print(f"El archivo Origen {archivo_origen} no existe")
#contar palabra de un archivo       
def contar_palabra(archivo):
    try:
        with open(archivo,"r") as f:
            contenido = f.read() #leemos todo el contenido
            palabras = contenido.split()
            print(f"el  archivo {archivo} contiene {len(palabras)} palabras")
    except FileNotFoundError:
        print(f"El archivo:  {archivo} no existe")
#Remplazar palabras en un archivo        
def remplazar_palabra(archivo_origen,palabra_buscar,palabra_remplazo,archivo_destino):
    try:
        with open(archivo_origen,"r") as origen:
            contenido = origen.read()
        
        #remplazar la palabra
        contenido_modificado = contenido.replace(palabra_buscar,palabra_remplazo)  
        #Guarda el contenido modificado en nuevo archivo
        with open(archivo_destino,"w") as destino:
            destino.write(contenido_modificado)
            print("Palabra Cambiada")
          
    except FileNotFoundError:
        print(f"El archivo:{archivo_origen} no existe")            

#Main
copiar_archivo("files/ejemplo3.txt","files/ejemplo2.txt") 
contar_palabra("files/ejemplo.txt")
remplazar_palabra("files/ejemplo.txt","Tlaxcala","Temuco","files/ejemplo2.txt")       
            