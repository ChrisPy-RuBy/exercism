#!/usr/bin/env bash

# determine appropriate position for the letter.
build_diamond () {
    letters="$1"
    length=${#1}
    mid_minus=$(($2 - 1))
    pos_start=$2
    pos_end=$2
    for (( i=0; i<$length; i++ )); do
        row=""
        for value in $(seq 1 $length); do
            if [[ $value == "$pos_start" ]] || [[ $value == "$pos_end" ]]; then
                row=$row"${letters:i:1}"
            else
                row="$row."
            fi
    done
    if [[ i -lt $mid_minus ]];then
        (( pos_start -= 1 ))
        (( pos_end += 1 ))
    elif [[ i -ge $mid_minus ]]; then
        (( pos_start += 1 ))
        (( pos_end -= 1 ))
    fi
    echo $row
done
}

find_mid () {
    length=$1
    if (( $length % 2 == 0 )); then
        echo "$(( length / 2))"
    else
        (( length -= 1 ))
        echo "$(( length / 2 + 1))"
    fi
    }

main () {
    letters=""
    width=0
    for letter in {A..Z}; do
        letters=$letters$letter
        if [[ $1 == "$letter" ]]; then
            width=$((${#letters} + ${#letters}-1))
            break
        fi
    done
    skip_first=$((${#letters}-2))
    for ((i=$skip_first; i>=0; i--)); do
        letters=$letters${letters:i:1}
    done
    mid=$(find_mid $width)
    build_diamond $letters $mid
}
main "$@"

