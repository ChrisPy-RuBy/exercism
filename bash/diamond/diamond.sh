#!/usr/bin/env bash

# determine appropriate position for the letter.
build_diamond () {
    test="ABCDEDCBA"
    length=${#test}
    mid=5
    mid_minus=$((mid - 1))
    pos_start=$mid
    pos_end=$mid
    for (( i=0; i<${#test}; i++ )); do
        row=""
        for value in $(seq 1 $length); do
            if [[ $value == "$pos_start" ]] || [[ $value == "$pos_end" ]]; then
                row=$row"${test:i:1}"
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
    row="$row\n"
    echo $row
done
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
    echo "$skip_first"
    for ((i=$skip_first; i>=0; i--)); do
        letters=$letters${letters:i:1}
    done
    echo $width $letters


}
#build_diamond "$@"
main "$@"

