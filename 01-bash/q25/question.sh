##
##  Gestion de datos con BASH
##  ===========================================================================
##
##  Cuantas tarjetas se vencen en el trimestre Q4 del año?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
awk '/Oct/{c++} /Nov/{c++}/Dec/{c++} END{print c+0}' *.txt