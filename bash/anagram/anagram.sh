#!/usr/bin/env bash
# set -x
# must not return itself.
# must not return capitalized versions
# if the length is different then definately not anagram


to_check=${1,,}
declare -A to_check
for((i=0; i<${#to_check};i++)); do
    to_check[${to_check:i:1}]+=1
done

create_lookup () {
    declare -A temp
    for((i=0; i<${#1};i++)); do
        temp[${1:i:1}]+=1
    done
    # now check against the starting word
    blacklist=0
    for key in "${!temp[@]}"; do
        b_value=${temp[$key]}
        a_value=${to_check[$key]}
        if [[ a_value -ne b_value ]]; then
            blacklist=1
        fi
    done
    echo "$blacklist"
    }

list_to_check=$2
whitelist=()

for word in $list_to_check; do
    # do some string tidying
    nword=${word,,}
    if [[ ${#word} -eq ${#to_check} ]] && [[ $nword != $to_check ]] ; then
        result=$(create_lookup "$nword")
        if [[ $result == "0" ]]; then
            whitelist=("${whitelist[@]}" "$word")

        fi
    fi
done

echo "${whitelist[@]}"
