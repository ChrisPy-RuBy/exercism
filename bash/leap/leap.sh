#!/usr/bin/env bash
#set -x          # useful debug
#set -u          # will exit if no parameter set

noargs=$#
# useful articles
# https://www.davidpashley.com/articles/writing-robust-shell-scripts/
# https://stackoverflow.com/questions/699576/validating-parameters-to-a-bash-script

if [[ $noargs != 1 ]] || [[ $1 == *[^0-9]* ]]; then
    echo 'Usage: leap.sh <year>'
    exit 1
fi

if [[ $(($1%4)) != 0 ]] || [[ $(($1%100)) == 0 ]]; then
    if [[ $(($1%400)) == 0 ]]; then
        echo true
    else
        echo false
    fi
else
    echo true
fi

