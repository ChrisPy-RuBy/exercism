#! usr/bin/env bash

function main () {
    # convert to lowercase
    var=${1,,}
    for i in {a..z}; do
        if ! [[ $i =~ [$var] ]]; then
            echo false; exit 0
        fi
    done
    echo true
}

main "$@"
