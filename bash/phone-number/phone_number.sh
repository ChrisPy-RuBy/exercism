#!/usr/bin/env bash

echo $1
clean=${1//[^[:word:]]/}
echo $clean

if [[ ${#clean} -eq 10 ]]; then
    echo "$clean"
else

    echo "${clean:1:10}"
fi


main () {
    # your main function code here
}
