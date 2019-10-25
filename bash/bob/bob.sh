#!usr/bin/env bash
# set -x
# rewrite this as a function.
# use a case statement
# Bob answers '"Sure.' if you ask him a question.
# He answers 'Whoa, chill out!' if you yell at him.
# He answers 'Calm down, I know what I'm doing!' if you yell a question at him.
# He says 'Fine. Be that way!' if you address him without actually saying anything.
# He answers 'Whatever.' to anything else.

answer1="Sure."
answer2="Whoa, chill out!"
answer3="Calm down, I know what I'm doing!"
answer4="Fine. Be that way!"
answer5="Whatever."

notabs="${1//[$'\t\r\n ']}"
var="${notabs//[1-9,\.!%\^*@#$:)\t\\]/}"
clean="${var// /}"

if [[ ${#notabs} -eq 0 ]]; then
   echo "$answer4" && exit 0
elif [[ ${#clean} -eq 0 ]]; then
   echo "$answer5" && exit 0
fi

function main () {
    if [[ $clean =~ \?$ ]]; then
        if [[ $clean =~ ^[^a-z]*$ ]] && [[ ${#clean} -gt 1 ]]; then
            echo "$answer3" && exit 0
        else
            echo "$answer1" && exit 0
        fi
    elif [[ $clean =~ ^[^a-z]*$ ]]; then
        echo "$answer2" && exit 0
    else
        echo "$answer5"
    fi
}

main "$clean"
