##
##  Gestion de datos con BASH
##  ===========================================================================
##
##  Cual el nombre  completo (fullname) del del dueño de la tarjeta 
##  3608-2968-5750-1980?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
#grep -w "3608-2968-5750-1980" bank.csv
grep "425-60-1543" person|awk -F"," '{gsub(/"/,"");print $5}'
