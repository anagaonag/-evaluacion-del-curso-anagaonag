##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, imprima la suma de la columna 2 para cada 
##  letra de la columna 4, ordnados alfabeticamente.
##
##  Rta/
##  a,114
##  b,40
##  c,91
##  d,65
##  e,79
##  f,110
##  g,35
##
##  No puede usar pandas en este ejercicio
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import csv
text = []
with open('data.csv', 'rt') as f:
    text += f.readlines()
text = [line.replace("\n","").split("\t") for line in text]
column2 = [row[1] for row in text]
column4 = [row[3] for row in text]
lista = [[element,column2[i]] for i in range(len(column4)) for element in column4[i].split(",")]
keys = set(row[0] for row in lista)
tuplas = []
for key in keys:
    sum = 0
    for i in range(len(lista)):
        if lista[i][0] == key:
            sum += int(lista[i][1])
    tuplas.append([key,sum])
for tupla in sorted(tuplas):
    print(str(tupla[0])+","+str(tupla[1]))
