#!usr/bin/env bash

var=$1
A=0
C=0
G=0
T=0

for (( i=0; i<${#var}; i++ )); do
    case ${var:$i:1} in
        A) ((A++));;
        C) ((C++));;
        G) ((G++));;
        T) ((T++));;
        *)
            printf "Invalid nucleotide in strand"
            exit 1
    esac
done

printf "A: %s\nC: %s\nG: %s\nT: %s" "$A" "$C" "$G" "$T" 
