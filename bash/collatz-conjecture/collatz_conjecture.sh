#/usr/bin/env bash
#set -x

# useful articles
# https://askubuntu.com/questions/385528/how-to-increment-a-variable-in-bash

var=$1

if [[ $# != 1 ]] || [[ $var -lt 1 ]]
then
    echo Error: Only positive numbers are allowed
    exit 1
fi

counter=0

while [[ $var != 1 ]]
do
    ((counter++))
    even=$(($var%2))
    if [[ $even == 0 ]]
    then
        var=$(($var/2))
    else
        var=$((($var*3)+1))
    fi
done

echo $counter

# odd mean n * 3 + 1
# even means n / 2

