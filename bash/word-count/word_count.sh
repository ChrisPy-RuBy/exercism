#!/usr/bin/env bash

declare -A dictionary

main () {
for word in $@; do
    if [[ -n "${dictionary[$word]}" ]]; then
         (( dictionary[$word] += 1 ))
     else
         dictionary["$word"]=1
     fi
done
for key in "${!dictionary[@]}"; do
    echo $key:  ${dictionary[$key]}
done | sort -rn
}

# clean input. Mostly...
# annoyingly \n, \t, etc are not being matched correctly.
preclean=${*//\\n/ }
lowercase=${preclean,,}
clean=${lowercase//[^0-9a-z\'\"]/ }
main "$clean"
