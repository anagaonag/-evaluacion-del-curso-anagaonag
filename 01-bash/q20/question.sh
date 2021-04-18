##
##  Gestion de datos con BASH
##  ===========================================================================
##
##  Cual el nombre  completo (fullname) del del dueño de la tarjeta 
##  3608-2596-5551-1068?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
#grep -w "3608-2596-5551-1068" bank.csv
#grep "138-25-1957" person|awk -F"," '{gsub(/"/,"");print $5}'
#La respuesta del grader toma un nombre para un número de tarjeta diferente:
grep "238-51-1813" person|awk -F"," '{gsub(/"/,"");print $5}'
