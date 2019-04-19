#!usr/bin/env bash

var=$1
length=${#var}

# create the total
sum () {
    sum=0
    for (( i=0; i<length; i++ )); do
        # this is a bit hard to understand 
        ((sum += $((${var:$i:1}**length))))
    done
}

check () {
    # decide if armstrong number or not.
    if (( $var == "$sum" )); then
        echo true
    else
        echo false
    fi
}

main() {

    var=$1
    length=${#var}
    sum
    check
}

main $1
