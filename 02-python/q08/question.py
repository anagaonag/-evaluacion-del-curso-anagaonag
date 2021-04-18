##
##  Programación en Python
##  ===========================================================================
##
##  Genere una lista de tuplas, donde cada tupla contiene en la primera 
##  posicion, el valor de la segunda columna; la segunda parte de la 
##  tupla es una lista con las letras (ordenadas y sin repetir letra) 
##  de la primera  columna que aparecen asociadas a dicho valor de la 
##  segunda columna. Esto es:
##
##  Rta/
##  ('0', ['C'])
##  ('1', ['A', 'B', 'D', 'E'])
##  ('2', ['A', 'D', 'E'])
##  ('3', ['A', 'B', 'D', 'E'])
##  ('4', ['B', 'E'])
##  ('5', ['B', 'C', 'D', 'E'])
##  ('6', ['A', 'B', 'C', 'E'])
##  ('7', ['A', 'C', 'D', 'E'])
##  ('8', ['A', 'B', 'E'])
##  ('9', ['A', 'B', 'C', 'E'])
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
    lista = sorted(set(lista))
    tuplas.append((key,lista))
for tupla in sorted(tuplas):
    print(repr(tupla))
