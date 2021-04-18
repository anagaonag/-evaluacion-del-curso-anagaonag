##
##  Programación en Python
##  ===========================================================================
##
##  Imprima la suma de la segunda columna del archivo `data.csv`.
##
##  Rta/
##  190
##
##  No puede usar pandas en este ejercicio
##
##  >>> Escriba su codigo a partir de este punto <<<
total=0
x=open('data.csv','r').readlines()
for i in range(len(x)):
    total+=int(x[i].split('\t')[1])
print(total)