##
##  Gestion de datos con BASH
##  ===========================================================================
##
##  Cuantas tarjetas se vencen en el trimestre Q1 del año?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
awk '/Jan/{c++} /Feb/{c++}/Mar/{c++} END{print c+0}' *.txt