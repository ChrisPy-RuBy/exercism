#!/usr/bin/env bash 

#useful articles
# https://stackoverflow.com/questions/13111967/shell-scripting-raise-to-the-power
# https://unix.stackexchange.com/questions/40786/how-to-do-integer-float-calculations-in-bash-or-other-languages-frameworks




if [ $1 == 'total' ] 
    then
        total="0"
        i="64"
        while [ $i -gt 0 ]
        do
        i=$[$i-1]
        var=$(echo 2^$i | bc)
        total=$(echo $total+$var | bc)
        done
    echo $total
    exit 0 
fi

error="Error: invalid input"
if [ $1 -gt 0 ] && [ $1 -lt 65 ]
    then
        let power=$1-1
        x=$(echo 2^$power | bc)
        echo $x
else
    echo $error
    exit 1
fi
