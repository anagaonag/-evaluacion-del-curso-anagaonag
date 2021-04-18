##
##  Programación en Python
##  ===========================================================================
##
##  Imprima la cantidad de registros por letra para la primera columna del 
##  archivo `data.csv`, ordenados alfabeticamente por la letra.
##
##  Rta/
##  A,8
##  B,7
##  C,5
##  D,6
##  E,14
##
##  No puede usar pandas en este ejercicio
##
##  >>> Escriba su codigo a partir de este punto <<<
texto = []
with open('data.csv', 'rt') as f:
    texto += f.readlines()
texto=[line.replace("\n","") for line in texto]
texto=[line.split("\t")[0] for line in texto]
keys=set(texto)
tuplas=[(key,texto.count(key)) for key in keys]
for tupla in sorted(tuplas):
    print(str(tupla[0])+","+str(tupla[1]))