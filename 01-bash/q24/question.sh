##
##  Gestion de datos con BASH
##  ===========================================================================
##
##  Cuantas tarjetas se vencen en el trimestre Q3 del año?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
awk '/Jul/{c++} /Aug/{c++}/Sep/{c++} END{print c+0}' *.txt