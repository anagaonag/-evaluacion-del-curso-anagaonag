##
##  Programación con Pandas
##  ===========================================================================
##
##  Imprima el promedio de la _c2 por cada letra de la _c1 
##  del archivo `tbl0.tsv`.
## 
##  Rta/
##  _c1
##  A    4.625000
##  B    5.142857
##  C    5.400000
##  D    3.833333
##  E    4.785714
##  Name: _c2, dtype: float64
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import pandas as pd
import os
x= pd.read_csv('tbl0.tsv', sep='\t')
x=x[['_c1', '_c2']]
df = x.sort_values(by='_c1')
df = df.groupby('_c1').mean()['_c2']
print(df)