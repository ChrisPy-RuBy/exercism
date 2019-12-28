#!/usr/bin/env bash

declare -A scrabble
scrabble["aeioulnrst"]=1
scrabble["dg"]=2
scrabble["bcmp"]=3
scrabble["fhvwy"]=4
scrabble["k"]=5
scrabble["jx"]=8
scrabble["qz"]=10


main () {
    score=0
    for ((i=0; i<${#1}; i++)); do
        letter=${1:i:1}
        for key in "${!scrabble[@]}"; do
            if [[ $letter =~ [$key] ]]; then
                value=${scrabble[$key]}
                (( score += value ))
            fi
        done
    done
    echo "$score"
}
main "$@"

