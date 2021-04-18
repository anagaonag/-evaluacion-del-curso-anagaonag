##
##  Programación con Pandas
##  ===========================================================================
##
##  Construya una tabla que contenga _c0 y una lista
##  separada por ',' de los valores de la columna _c5a
##  y _c5b (unidos por ':') de la tabla tbl2.tsv
## 
##  Rta/
##      _c0                                lista
##  0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
##  1     1              aaa:3,ccc:2,ddd:0,hhh:9
##  ...
##  38   38                    eee:0,fff:9,iii:2
##  39   39                    ggg:3,hhh:8,jjj:5
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import pandas as pd

data = pd.read_csv('tbl2.tsv' , sep='\t')
xn = sorted(pd.unique(data._c0))
serie = pd.Series(xn, name= '_c0')
data['x2'] =  data['_c5a'].astype(str) +':'+ data['_c5b'].astype(str)
listas = []
for n in xn:
    temp = sorted(data[data['_c0'] == n].x2)
    empty = ''
    for num, let in enumerate(temp):
        if num == len(temp)-1:
            empty = empty + str(let)
        else:
            empty = empty + str(let) + ','
    listas.append(empty)
lista = pd.Series(listas, name='lista')
tabla = pd.concat([serie , lista], axis=1)
print(tabla)
