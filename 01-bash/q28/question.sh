##
##  Gestion de datos con BASH
##  ===========================================================================
##
##  Cuantas veces aparece el número 1192 en el segundo grupo de digitos de las 
##  tarjetas de  credito?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
#cut -d "," -f6 *.txt | cut -d "-" -f2 | awk '/-04-/{c++} /-05-/{c++}/-06-/{c++} END{print c+0}' 
awk '/-1192-/{c++}END{print c+0}' *.txt