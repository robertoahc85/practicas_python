import csv
#leer un archivo
with open("files/csv/people.csv", "r", newline="") as archivo:
    lector_csv = csv.reader(archivo)
    for fila in lector_csv:
        print(fila)
#Escribir en archivo csv
with open("files/csv/people2.csv", "w", newline="") as file:
    escritor_csv = csv.writer(file)
    escritor_csv.writerow(["Nombre","Apellido","Ciudad"])
    escritor_csv.writerow(["Fernando","Ruiz","Osorno"])
    escritor_csv.writerow(["Eduardo","Valenzuela","Antofagasta"])
    escritor_csv.writerow(["Nicole","Rodriguez","Temuco"])
#Agregar un registro  a un archivo csv   
with open("files/csv/people.csv", "a", newline="") as f:
    escritor_csv=csv.writer(f)
    escritor_csv.writerow(["Cristian","Castillo","Concepcion"])
    
    