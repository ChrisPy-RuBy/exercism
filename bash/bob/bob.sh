#!usr/bin/env bash

# if question == 'chill'
# if caps == Whoa, chill out!
# yell question == 'Calm down, I know what I'm doing!'
# no question == "Fine. Be that way!"
# else == 'Whatever'

if [[ $1 =~ ^[^a-z]*$ ]] && [[ $1 =~ .*\? ]]; then
    echo "Calm down, I know what I'm doing!"
elif [[ $1 =~ ^[^a-z]*$ ]]; then
    echo "Whoa, chill out!"
elif [[ $1 =~ .*\? ]]; then 
    echo "Sure."
elif [[ $1 == "" ]]; then
    echo "Fine. Be that way!"
else 
    echo "Whatever."
fi
