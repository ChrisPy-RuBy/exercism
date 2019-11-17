#!/usr/bin/env bash

main () {
    strand1=$1
    strand2=$2
    wrongchars=0

    if [[ "${#strand1}" != "${#strand2}" ]]; then
        echo "left and right strands must be of equal length"; exit 1
    elif [[ $# == 0 ]]; then
        echo "Usage: hamming.sh <string1> <string2>"; exit 1
    fi

    for (( i=0; i<${#strand1};i++ )); do
        if [[ ${strand1:$i:1} != "${strand2:$i:1}" ]]; then
            ((wrongchars++))
        fi
    done
    echo $wrongchars
}

main "$@"
