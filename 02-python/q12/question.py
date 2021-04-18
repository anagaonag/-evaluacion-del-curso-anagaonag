##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, imprima por cada fila, la columna 1 y la suma 
##  de los valores de la columna 5.
##
##  Rta/
##  E,22
##  A,14
##  B,14
##  ....
##  C,8
##  E,11
##  E,16
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
column5 = [row[4] for row in text]
for i in range(len(column1)):
    sum = 0
    valores = [element.split(":")[1] for element in column5[i].split(",")]
    for val in valores:
        sum += int(val)
    print(column1[i]+","+str(sum))


