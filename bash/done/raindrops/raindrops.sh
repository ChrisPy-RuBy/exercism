#!/usr/bin/env bash

main () {
    results=""
    if [[ $(($1%3)) == 0 ]]; then
    results="Pling"; fi

    if [[ $(($1%5)) == 0 ]]; then
    results=$results"Plang"; fi

    if [[ $(($1%7)) == 0 ]]; then
    results=$results"Plong"; fi

    if [[ $results == "" ]]; then
    results=$1; fi

    echo "$results"
}

main "$@"
