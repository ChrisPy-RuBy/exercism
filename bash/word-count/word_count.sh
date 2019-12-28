#!/usr/bin/env bash

declare -A dictionary

main () {
for word in $@; do
    if [[ -n "${dictionary[$word]}" ]]; then
         (( dictionary[$word] += 1 ))
     else
         dictionary[$word]=1
     fi
done
for key in "${!dictionary[@]}"; do
    echo $key:  ${dictionary[$key]}
done | sort -rn
}

# call main with all of the positional arguments
main "$@"
