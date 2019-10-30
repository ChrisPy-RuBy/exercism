#!/usr/bin/env bash

if [[ "${#1}" -gt 0 ]]; then
    input=$1
else
    exit 0
fi

declare -A dna
dna=(["G"]="C" ["C"]="G" ["T"]="A" ["A"]="U")

main () {
    for ((i=0; i<${#input}; i++)); do
        rna_letter=${dna[${input:$i:1}]}
        if [[ $rna_letter == "" ]]; then
            echo "Invalid nucleotide detected."; exit 1
        else
            echo "$rna_letter"
        fi
    done
   }


main "$@"
