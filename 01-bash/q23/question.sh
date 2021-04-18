##
##  Gestion de datos con BASH
##  ===========================================================================
##
##  Cuantas tarjetas se vencen en el trimestre Q2 del año?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
awk '/Apr/{c++} /May/{c++}/Jun/{c++} END{print c+0}' *.txt