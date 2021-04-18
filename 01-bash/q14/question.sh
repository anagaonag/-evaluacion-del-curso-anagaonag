##
##  Gestion de datos con BASH
##  ===========================================================================
##
##  Cual es la 'ciudad (estado)' en la posicion 2 del archivo 'person', si el 
##  archivo se organiza alfabeticamente por el campo 'ssn'?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
cat person|sort -k1,1n|awk -F'""' 'NR == 2'|awk -F"," '{gsub(/"/,"");print $3}'
#cat person|sort -k1,1n|awk -F'""' 'NR == 1'|awk -F"," '{gsub(/"/,"");print $3}'