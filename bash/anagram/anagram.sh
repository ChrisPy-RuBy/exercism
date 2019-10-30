#!/usr/bin/env bash


to_check=$1
list_to_check=$2

whitelist=""

for word in $list_to_check; do
    blacklist=0
    for ((i=0; i<${#to_check}; i++)); do
        if [[ ${to_check} =~ [^$word] ]]; then
            blacklist=1
        fi
    done
    if [[ $blacklist -eq 0 ]]; then
        whitelist="$whitelist $word"
    fi
done

echo $whitelist

#main () {
#    # your main function code here
#  }
main "$@"

