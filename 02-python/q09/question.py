##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv, imprima una tabla en formato CSV que contenga 
##  la cantidad de registros en que aparece cada clave de la columna 5.
##
##  Rta/
##  aaa,13
##  bbb,16
##  ccc,23
##  ddd,23
##  eee,15
##  fff,20
##  ggg,13
##  hhh,16
##  iii,18
##  jjj,18
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
column5 = [row[4] for row in text]
lista = [element for line in column5 for element in line.split(",")]
keys = [element.split(":")[0] for element in lista]
keys_uniq = set(keys)
tuplas = [(key,keys.count(key)) for key in keys_uniq]
for tupla in sorted(tuplas):
    print(str(tupla[0])+","+str(tupla[1]))



