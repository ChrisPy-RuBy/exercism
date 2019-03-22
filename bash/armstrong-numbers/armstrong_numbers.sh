#!usr/bin/env bash

var=$1
length=${#var}
sum=0

# create the total
for (( i=0; i<length; i++ )); do
    # this is a bit hard to understand 
    ((sum += $((${var:$i:1}**length))))
done
# decide if armstrong number or not.
if [[ $var == "$sum" ]]; then
    echo true
else
    echo false
fi
