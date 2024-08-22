import csv
#escribe un csv incluyendo cabecera y los datos
def escribir_csv(filename,datos):
    with open(filename,mode="w",newline="") as file:
        escritor_csv= csv.writer(file) #invoncar la funcion de escribir de la libreria csv
        escritor_csv.writerow(["Nombre","Apellido","Ciudad"])#Escribimos a la cabecera
        for fila in datos:#recorremos los datos recibidos
            escritor_csv.writerow(fila) #Datos
        print("Archivo csv creado con exito ")
#leer archivo csv
def leer_csv(filename):
    print("======Contenido del archivo CSV=========")
    with open(filename,mode="r",newline="") as file:
        lector_csv= csv.reader(file)
        for fila in lector_csv:
            print(fila) 
            
#Agregar un registro al final del archivo
def agregar_csv(filename,registro): 
    with open(filename,mode="a",newline="") as file: 
        escritor_csv=csv.writer(file) 
        escritor_csv.writerow(registro) 
        print("Nuevo registro Agregado")             

datos_iniciales = [["Moises","Barrera","Santiago"],["Edgar","Carrion","Osorno"],["Cristopher","Sanchez","Santiago"]] 
nombre_archivo = "files/csv/students.csv"
registro_agregar = ['Armin',"Cano","Villarrica"]
registro_agregar2 = ['Jose',"Vinuela","Villarrica"]
escribir_csv(nombre_archivo,datos_iniciales)
leer_csv(nombre_archivo)
agregar_csv(nombre_archivo,registro_agregar)
leer_csv(nombre_archivo)
agregar_csv(nombre_archivo,registro_agregar2)



