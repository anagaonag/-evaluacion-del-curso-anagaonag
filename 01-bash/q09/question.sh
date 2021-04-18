##
##  Gestion de datos con BASH
##  ===========================================================================
##
##  Cual es el valor del campo 'ccn' del archivo 'data.csv' para el 
##  registro 10?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
awk -F'""' 'NR == 11' data.csv|awk -F"," '{gsub(/"/,"");print $1}'