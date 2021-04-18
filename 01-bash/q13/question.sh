##
##  Gestion de datos con BASH
##  ===========================================================================
##
##  Cual es la 'ciudad (estado)' en la posicion 1 del archivo 'person', si el 
##  archivo se organiza alfabeticamente por el campo 'ssn'?
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
#awk 'NR == 1; NR > 1 {print $0 | "sort -1"}' person
#cat person| sort|cut -d, -f3|head -n 1| tr -d '"'
#cat person|sort -k1,1n|awk -F"," '{print $3}'
cat person|sort -k1,1n|awk -F'""' 'NR == 1'|awk -F"," '{gsub(/"/,"");print $3}'
#cat person| awk -F"," '{print $3}'|head -n 1| tr -d '"'|sort -k1,1n
#sort -k3| awk -F"," 'NR == 3' '{print $1}' person
#awk -F'""' 'NR == 3' person|awk -F"," '{gsub(/"/,"");print $3}'
#head -n1 person
#tail -n+2 person | sort -k1n,1
#head -n 2 person 
#tail -n+2 person | sort -k1 
#tail -n 1 person|sort -t ',' -k1 person
#tail +2 person| awk '{print $NF "\t" $0}' person | sort | cut -f1-
#| sort -k1,1n
#awk 'NR == 2' person|awk -F"," '{print $3}'
#tail -n +2 person
#sort -k -1 person
#sort -1k person| awk -F'""' 'NR == 1' person|awk -F"," '{gsub(/"/,"");print $3}'