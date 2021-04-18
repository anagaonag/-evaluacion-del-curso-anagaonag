##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, imprima la suma de la columna 2 por cada letra 
##  de la primera columna, ordneados alfabeticamente.
##
##  Rta/
##  A,37
##  B,36
##  C,27
##  D,23
##  E,67
##
##  No puede usar pandas en este ejercicio
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import csv
text=[]
with open('data.csv', 'rt') as f:
    text += f.readlines()
text = [line.replace("\n","").split("\t") for line in text]
column1 = [row[0] for row in text]
column2 = [row[1] for row in text]
keys = set(column1)
tuplas = []
for key in keys:
    sum = 0
    for i in range(len(column1)):
        if column1[i] == key:
            sum += int(column2[i])
    tuplas.append((key,sum))
for tupla in sorted(tuplas):
    print(str(tupla[0])+","+str(tupla[1]))   
