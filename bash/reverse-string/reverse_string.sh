#!/usr/bin/env bash
var=$1
rev=""
i=0
len="${#var}"

if [[ $var == "" ]]
then 
    echo ""
else
    while [ $i -lt $len ]
    do
        rev=${var:i++:1}$rev
    done
    echo $rev
fi


