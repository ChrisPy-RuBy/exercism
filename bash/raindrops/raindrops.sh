#!/usr/bin/env bash
#set -x

var=$1
results=""


if [[ $(($var%3)) == 0 ]]
then
    results="Pling"
fi

if [[ $(($var%5)) == 0 ]]
then
    results=$results"Plang"
fi

if [[ $(($var%7)) == 0 ]]
then 
    results=$results"Plong"
fi

if [[ $results == "" ]]
then
    results=$var
fi

echo $results
