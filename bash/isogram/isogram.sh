#!/usr/bin/env bash

declare -A letter_count

main () {
    for ((i=0; i<${#1}; i++)); do
        letter=${1:i:1}
        if [[ $letter =~ [a-z] ]]; then
            if [[ -n ${letter_count[$letter]} ]]; then
                echo "not isogram"; exit 0
            else
                letter_count[$letter]=1
            fi
        fi
    done
    echo "isogram"
}

main "$@"

