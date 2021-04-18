##
##  Programación en Bash
##  ===========================================================================
##
##  Usando los archivos `data1.csv`, `data2.csv`, `data3.csv`, escriba en el
##  archivo `script.sh`  un programa en Bash que imprima en pantalla
##  la siguiente salida por linea:
## 
##  * El nombre del archivo.
##  * El número de la línea procesada.
##  * La letra de la primera columna del archivo.
##  * La cadena de tres letras y el valor asociado de la columna 2 del archivo original. 
##
##  Note que se genera una línea de salida por cada cadena de tres letras.
##   
##  Rta/
##
##  data1.csv,1,E,jjj:3
##  data1.csv,1,E,bbb:0
##  ...
##  data3.csv,3,B,hhh:1
##  data3.csv,3,B,ddd:2
##
##  >>> Escriba su codigo a partir de este punto <<<
##
for i in $(ls)
do
    cont=0
    if [[ $i =~ (.*)csv$ ]]
    then
        #echo $i
        while IFS= read -r line
        do
            if [ -n "$line" ]; then
                #echo $line
                let cont=$cont+1
                #echo $line 
                echo $line > tmp.1
                col2=$(awk '{split($0,nombre," ")} {print nombre[2]}' tmp.1)
                IFS=',' read -ra letter3 <<< "$col2"
                for j in "${letter3[@]}"; do
                    echo $i","$cont","${line:0:1}","$j 
                done  
            fi
            
        done < $i
    fi 
done
rm tmp.1