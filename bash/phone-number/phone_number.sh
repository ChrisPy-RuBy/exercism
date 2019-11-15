#!/usr/bin/env bash
# set -x
#  ok so they want it in this format.
# This looks like a regex thing to me
# so we either have 10 or 11 numbers that
# we need to match
# [1]NXX-NXX-XXXX N=2-9, X=0-9


error="Invalid number.  [1]NXX-NXX-XXXX N=2-9, X=0-9"

clean=${1//[^[:word:]]/}

if [[ ${clean} =~ ^1{0,1}[2-9]{1}[0-9]{2}[2-9]{1}[0-9]{2}[0-9]{4}$ ]]; then
    if [[ ${#clean} -eq 11 ]]; then
        echo "${clean:1:10}"
    else
        echo "$clean"
    fi
else
    echo "$error"; exit 1
fi

