##
##  Gestion de datos con BASH
##  ===========================================================================
##
##  Cuantas personas nacieron en el trimestre Q2 del año?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
cut -d "," -f6 person | cut -d "-" -f2 | awk '/-04-/{c++} /-05-/{c++}/-06-/{c++} END{print c+0}' person