#! usr/bin/env bash
# set -x

# Notes: could do this with
# regex, look ahead assertions. Can't do this with bash but can do with grep and awk
# for loop

declare -a arr=("a" "b" "c" "d" "e" "f" "g" "h"
                "i" "j" "k" "l" "m" "n" "o" "p"
                "q" "r" "s" "t" "u" "v" "w" "y" "x" "z")

function main () {
    # jesus this is esoteric!
    var=${*,,}
    for i in "${arr[@]}"; do
        if [[ $i =~ [$var] ]]; then
            true
        else
            echo false && exit 0
        fi
    done
    echo true && exit 0
}


main "$@"
