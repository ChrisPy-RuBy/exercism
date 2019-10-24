#! usr/bin/env bash

declare -a arr=("a" "b" "c" "d" "e" "f" "g" "h"
                "i" "j" "k" "l" "m" "n" "o" "p"
                "q" "r" "s" "t" "u" "v" "w" "y"
                "x" "z")

function main () {
    # convert to lowercase
    var=${1,,}
    for i in "${arr[@]}"; do
        if ! [[ $i =~ [$var] ]]; then
            echo false && exit 0
        fi
    done
    echo true
}

main "$@"
