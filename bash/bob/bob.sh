#!usr/bin/env bash

declare -A answers
answers[sure]="Sure."
answers[whoa]="Whoa, chill out!"
answers[calm]="Calm down, I know what I'm doing!"
answers[fine]="Fine. Be that way!"
answers[whatever]="Whatever."

function main () {

    notabs="${1//[[:space:]]}"
    clean="${notabs//[1-9,\.!%\^*@#$:)\\]/}"

    if [[ ${#notabs} -eq 0 ]]; then
        echo "${answers[fine]}" && exit 0
    elif [[ ${#clean} -eq 0 ]]; then
        echo "${answers[whatever]}" && exit 0
    fi

    if [[ $clean =~ \?$ ]]; then
        if [[ $clean =~ ^[^a-z]*$ ]] && [[ ${#clean} -gt 1 ]]; then
            echo "${answers[calm]}" && exit 0
        else
            echo "${answers[sure]}" && exit 0
        fi
    elif [[ $clean =~ ^[^a-z]*$ ]]; then
        echo "${answers[whoa]}" && exit 0
    else
        echo "${answers[whatever]}"
    fi
}

main "$@"
