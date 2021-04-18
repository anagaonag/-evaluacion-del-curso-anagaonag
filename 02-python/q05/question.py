##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, imprima el valor maximo y minimo de la columna
##  2 por cada letra de la columa 1.
##
##  Rta/
##  A,9,1
##  B,9,1
##  C,9,0
##  D,7,1
##  E,9,1
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
    min = int(column2[0])
    max = int(column2[0])
    for i in range(len(column1)):
        if column1[i] == key:
            if int(column2[i]) < min:
                min = int(column2[i])
            if int(column2[i]) > max:
                max = int(column2[i])
    tuplas.append((key,max,min))
for tupla in sorted(tuplas):
    print(str(tupla[0])+","+str(tupla[1])+","+str(tupla[2])) 

