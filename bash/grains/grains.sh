#!/usr/bin/env bash 
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
        python -c "x = 2**$power; print x"
else
    echo $error
    exit 1
fi
