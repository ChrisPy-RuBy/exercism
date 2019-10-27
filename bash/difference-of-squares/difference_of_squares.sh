#!/usr/bin/env bash

square_of_sum () {
    total=0
    for i in $(seq "$2"); do
        total=$((total+i))
    done
    echo "$((total**2))"
  }

sum_of_squares () {
    total=0
    for i in $(seq "$2"); do
        total=$((total+i**2))
    done
    echo "$total"
  }


if [[ $1 == 'square_of_sum' ]]; then
    square_of_sum "$@"
elif [[ $1 == 'sum_of_squares' ]]; then
    sum_of_squares "$@"
elif [[ $1 == 'difference' ]]; then
    x=$(square_of_sum "$@")
    y=$(sum_of_squares "$@")
    echo $((x-y))
fi


