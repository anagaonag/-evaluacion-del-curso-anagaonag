##
##  Programación con Pandas
##  ===========================================================================
##
##  Construya una tabla que contenga _c0 y una lista
##  separada por ',' de los valores de la columna _c4
##  del archivo `tbl1.tsv`.
##
##  Rta/
##      _c0    lista
##  0     0    b,f,g
##  1     1    a,c,f
##  ...
##  38   38      d,e
##  39   39    a,d,f
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
import pandas as pd
data = pd.read_csv('tbl1.tsv' , sep='\t')
xn = sorted(pd.unique(data._c0))
serie = pd.Series(xn , name = '_c0')
listas = []
for n in xn:
    temp = sorted(data[data['_c0'] == n]._c4)
    empty = ""
    for num, let in enumerate(temp):
        if num == len(temp)-1:
            empty = empty + str(let)
        else:
            empty = empty + str(let)+","            
    listas.append(empty)
lista = pd.Series(listas, name = 'lista')
tabla = pd.concat([serie , lista] , axis = 1)
print(tabla)

