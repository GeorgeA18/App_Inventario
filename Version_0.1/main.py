import os
import csv



"---------------------------------------------------------------------------------------"

archivo = open("ArchivosPruebas\\hoja1.csv","r")

lectura = archivo.read()

print(lectura)
















"""
with open("ArchivosPruebas\\hoja1.csv") as archivo:

    lineas = csv.reader(archivo)

    for x in lineas:
        print(x)

"""