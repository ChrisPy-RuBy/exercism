#!/usr/bin/env bash
# create another lookup for word to be checked
# check against anagram
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

main () {
    # create a anagram lookup
    to_check_v=${1,,}
    declare -A to_check
    for((i=0; i<${#to_check_v};i++)); do
        to_check[${to_check_v:i:1}]+=1
    done

    list_to_check=$2
    whitelist=()

    for word in $list_to_check; do
        # do some string tidying
        nword=${word,,}
        if [[ ${#word} -eq ${#to_check_v} ]] && [[ $nword != $to_check_v ]] ; then
            result=$(create_lookup "$nword")
            if [[ $result == "0" ]]; then
                whitelist=("${whitelist[@]}" "$word")
            fi
        fi
    done
    echo "${whitelist[@]}"
}

main "$@"

