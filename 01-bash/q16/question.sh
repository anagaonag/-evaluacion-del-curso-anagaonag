##
##  Gestion de datos con BASH
##  ===========================================================================
##
##  Cuantos registros quedan en el archivo 'person' si se eliminan los 
##  registros con 'city' = 'Albuquerque (New Mexico)'?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
grep -v Albuquerque person>person2
grep -v fullname person2>person3
grep -c "^" person3