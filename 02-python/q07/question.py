##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, genera una lista de tuplas que asocien las 
##  columnas 0 y 1. Cada tupla contiene un valor posible de la columna 2 y una
##  lista con todas las letras asociadas (columna 1) a dicho valor de la 
##  columna 2.
##
##  Rta/
##  ('0', ['C'])
##  ('1', ['E', 'B', 'D', 'A', 'A', 'E'])
##  ('2', ['A', 'E', 'D'])
##  ('3', ['A', 'B', 'D', 'E', 'E'])
##  ('4', ['E', 'B'])
##  ('5', ['B', 'C', 'D', 'D', 'E', 'E', 'E'])
##  ('6', ['C', 'E', 'A', 'B'])
##  ('7', ['A', 'C', 'E', 'D'])
##  ('8', ['E', 'E', 'A', 'B'])
##  ('9', ['A', 'B', 'E', 'C'])
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
keys = set(column2)
tuplas = []
for key in keys:
    lista = []
    for i in range(len(column2)):
        if column2[i] == key:
            lista.append(column1[i])
    tuplas.append((key,lista))
for tupla in sorted(tuplas):
    print(repr(tupla))
