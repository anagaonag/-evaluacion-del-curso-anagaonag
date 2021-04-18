##
##  Programación con Pandas
##  ===========================================================================
##
##  Si la columna _c0 es la clave en los archivos `tbl0.tsv`
##  y `tbl2.tsv`, compute la suma de tbl2._c5b por cada
##  valor en tbl0._c1.
## 
##  Rta/
##  _c1
##  A    146
##  B    134
##  C     81
##  D    112
##  E    275
##  Name: _c5b, dtype: int64
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import numpy as np
import pandas as pd
import csv
datos= pd.read_csv('tbl2.tsv', sep='\t', header=0 )
datos1= pd.read_csv('tbl0.tsv', sep='\t', header=0 )
datos.sort_values(['_c0','_c5b'],inplace=True)
Tabla=datos[['_c0','_c5b']].groupby('_c0')['_c5b'].apply(lambda x: x.sum()).reset_index()
Tablam=pd.merge(datos1,Tabla,on='_c0')
Tablam.sort_values(['_c1','_c5b'],inplace=True)
Tablaf=Tablam.groupby("_c1")["_c5b"].sum()
print(Tablaf)



