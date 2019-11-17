#!/usr/bin/env bash
set -x
var=$1
rev=""
i=0
len="${#var}"

if [[ $var == "" ]]
then 
    echo ""
else
    # counter increments up to the length
    while [ $i -lt $len ]
    do
        # get the correct letter and add the rest of the 
        # reverse string to it
        rev=${var:i++:1}$rev
    done
    echo $rev
fi


