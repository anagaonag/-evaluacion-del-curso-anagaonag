##
##  Gestion de datos con BASH
##  ===========================================================================
##
##  Cuantas personas nacieron en el trimestre Q1 del año?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
cut -d "," -f6 person | cut -d "-" -f2 | awk '/-01-/{c++} /-02-/{c++}/-03-/{c++} END{print c+0}' person