!/usr/bin/env bash

x=3598215088

main () {
    echo "$x"
    sum=0
    index=0
    for number in {10..1}; do
        multi=$((${x:$index:1} * $number))
        (( sum += multi ))
        (( index += 1 ))
        echo $sum
    done
    if (( $sum % 11 == 0  )); then
        echo "True"
    else
        echo "$sum False"
    fi
}

main "$@"

