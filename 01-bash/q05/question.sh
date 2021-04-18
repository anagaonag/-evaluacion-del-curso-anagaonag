##
##  Gestion de datos con BASH
##  ===========================================================================
##
##  Cual es el valor del campo 'key' del archivo 'data.csv' para el 
##  registro 3?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
awk -F'""' 'NR == 4' data.csv|awk -F"," '{gsub(/"/,"");print $3}'