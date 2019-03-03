#!/usr/bin/env bash

#set -x

strand1=$1
strand2=$2
len1="${#strand1}"
len2="${#strand2}"
i=0
wrongcharacters=0

if [[ $len1 != "$len2" ]]
then
    echo "left and right strands must be of equal length"
    exit 1
elif [[ $# == 0 ]]
then
    echo "Usage: hamming.sh <string1> <string2>"
    exit 1
fi

if [[ $strand1 = "$strand2" ]]
then
    echo $wrongcharacters
else
    while [ $i -lt "$len1" ]
    do
        totest1=${strand1:$i:1}
        totest2=${strand2:$i:1}
        if [[ $totest1 != "$totest2" ]]
        then
            ((wrongcharacters++))
        fi
        ((i++))
    done
    echo $wrongcharacters
fi
