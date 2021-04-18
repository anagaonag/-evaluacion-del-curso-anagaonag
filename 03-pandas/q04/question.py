##
##  Programación con Pandas
##  ===========================================================================
##
##  Imprima una lista con los valores unicos de la columna _c4 de 
##  del archivo `tbl1.csv` en mayusculas.
## 
##  Rta/
##  ['A', 'B', 'C', 'D', 'E', 'F', 'G']
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import pandas as pd
import os
x= pd.read_csv('tbl1.tsv', sep='\t')
m = [m.upper() for m in x['_c4'].sort_values().drop_duplicates()]
print(m)
