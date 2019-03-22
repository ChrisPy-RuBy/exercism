#!usr/bin/env bash

var=$1
length=${#var}
sum=0

for (( i=0; i<length; i++ )); do
    (( sum += $((${var:$i:1}**length))))
done
if [[ $var == "$sum" ]]; then
    echo true
else
    echo false
fi
