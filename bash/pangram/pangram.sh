#! usr/bin/env bash
set -x
result=false

# Notes: could do this with
# regex
# for loop
# some sorting algorython

function main(){
    var=$*
    echo $var
    for(( i=0; i<${#var}; i++)); do
        echo "${var:$i:1}"
        done
    echo $result
} 


main $@ 
