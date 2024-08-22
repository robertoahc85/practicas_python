import csv
#lectura de archivos csv
with open('files/csv/alumnos.csv','r') as archivo_csv:
    lector= csv.reader(archivo_csv)
    for fila in lector:
        print(fila)
#Escribir en un archivo csv
 
datos = [["nombre", "edad",], ["edgar", 34], ["Gonzalo", 33]]
with open("files/csv/nuevo_datos.csv", "w", newline="") as archivo_csv:
    escribir = csv.writer(archivo_csv)
    for fila in datos:
        escribir.writerow(fila)   
     