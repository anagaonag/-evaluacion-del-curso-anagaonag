##
##  Gestion de datos con BASH
##  ===========================================================================
##
##  Cual el nombre  completo (fullname) del del dueño de la tarjeta 
##  3608-2181-4994-1181?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
#grep -w "3608-2181-4994-1181" bank.csv
grep "116-81-1858" person|awk -F"," '{gsub(/"/,"");print $5}'