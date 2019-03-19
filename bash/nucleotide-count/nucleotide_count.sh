#!usr/bin/env bash

var=$1
A=0
C=0
G=0
T=0

# tried to do this with a case statement but the syntax
# was too horrible!
for (( i=0; i<${#var}; i++ )); do
    if [[ ${var:$i:1} == "A" ]]; then
        ((A++))
    elif [[ ${var:$i:1}  == "C" ]]; then
        ((C++))
    elif [[ ${var:$i:1} == "G" ]]; then
        ((G++))
    elif [[ ${var:$i:1} == "T" ]]; then
        ((T++))
    else
        printf "Invalid nucleotide in strand" && exit 1
    fi
done

printf "A: %s\nC: %s\nG: %s\nT: %s" "$A" "$C" "$G" "$T" 
