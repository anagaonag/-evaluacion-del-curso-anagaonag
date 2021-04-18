##
##  Gestion de datos con BASH
##  ===========================================================================
##
##  Cual es el valor del campo 'validthru' del archivo 'data.csv' para 
##  el registro 2?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
awk -F'""' 'NR == 3' data.csv|awk -F"," '{gsub(/"/,"");print $2}'