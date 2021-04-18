##
##  Programación con Pandas
##  ===========================================================================
##
##  Construya una tabla que contenga _c1 y una lista
##  separada por ':' de los valores de la columna _c2
##  para el archivo `tbl0.tsv`.
##
##  Rta/
##    _c0                        lista
##  0   A              1:1:2:3:6:7:8:9
##  1   B                1:3:4:5:6:8:9
##  2   C                    0:5:6:7:9
##  3   D                  1:2:3:5:5:7
##  4   E  1:1:2:3:3:4:5:5:5:6:7:8:8:9
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
import pandas as pd
data = pd.read_csv('tbl0.tsv' , sep='\t')
letters = sorted(pd.unique(data._c1))
serie = pd.Series(letters , name = '_c0')
listas = []
for letter in letters:
    temp = sorted(data[data['_c1'] == letter]._c2)
    empty = ""
    for num, let in enumerate(temp):
            if num == len(temp)-1:
                empty = empty + str(let)
            else:
                empty = empty + str(let)+":"                                      
    listas.append(empty)
lista = pd.Series(listas, name = 'lista')
tabla = pd.concat([serie , lista] , axis = 1)
print(tabla)

