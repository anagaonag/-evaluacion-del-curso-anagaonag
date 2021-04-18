##
##  Programación en Python
##  ===========================================================================
##
##  La columna 5 del archvio `data.csv` codifica un diccionario donde cada
##  cadena de tres letras corresponde a una clave y el valor despues del
##  caracter `:` corresponde al valor asociado a la clave. Por cada clave,
##  obtenga el valor asociado mas pequeño y el valor asociado mas grande 
##  computados sobre todo el archivo. 
##
##  Rta/
##  aaa,0,6
##  bbb,4,7
##  ccc,0,1
##  ddd,5,5
##  eee,0,0
##  fff,4,9
##  ggg,3,3
##  hhh,6,8
##  iii,2,7
##  jjj,2,5
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
values = [element.split(":")[1] for element in lista]
keys_uniq = set(keys)
tuplas = []
for key in keys_uniq:
    min = int(values[0])
    max = int(values[0])
    for i in range(len(values)):
        if keys[i] == key:
            if int(values[i]) < min:
                min = int(values[i])
            if int(values[i]) > max:
                max = int(values[i])
    tuplas.append((key,min,max))
for tupla in sorted(tuplas):
    print(str(tupla[0])+","+str(tupla[1])+","+str(tupla[2])) 


