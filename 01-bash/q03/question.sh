##
##  Gestion de datos con BASH
##  ===========================================================================
##
##  Cual es el valor del campo 'ccn' del archivo 'data.csv' para el primer 
##  registro?
## 
##  >>> Escriba su codigo a partir de este punto <<<
awk -F'""' 'NR == 2' data.csv|awk -F"," '{gsub(/"/,"");print $1}'