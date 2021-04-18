##
##  Gestion de datos con BASH
##  ===========================================================================
##
##  Cuantos registros tiene el archivo 'data.csv'?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
tail -n +2  data.csv>data1.csv
grep -c "^" data1.csv
