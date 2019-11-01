#!/usr/bin/env bash

count_sides () {
    counter=0
    if [[ $3 -eq $2 ]]; then
        ((counter++))
    fi
    if [[ $3 -eq $4 ]]; then
        ((counter++))
    fi
    if [[ $2 -eq $4 ]]; then
        ((counter ++))
    fi
    echo "$counter"
}

if [[ -z $1 ]]; then
    triangle="**Unknown triangle**"
elif [[ -n $1 ]]; then
    triangle=$1
fi

case $triangle in
    "equilateral")
        if [[ $(count_sides "$@") -eq 3 ]]; then
            echo true
        else
            echo false; fi;;
    "isosceles")
        if [[ $(count_sides "$@") -eq 1 ]]; then
            echo true
        else
            echo false; fi;;
    "scalene")
        if [[ $(count_sides "$@") -eq 0 ]]; then
            echo true
        else
            echo false; fi;;
    *) echo "Herp derp"
esac

