#!/usr/bin/env bash

# useful articles
# https://www.lifewire.com/pass-arguments-to-bash-script-2200571 
# https://aty.sdsu.edu/bibliog/latex/debian/bash.html
# http://tldp.org/LDP/abs/html/string-manipulation.html -> docs on string manip

# regex for characters that aren't letters or numbers
clean=${@//[^a-zA-Z0-9]/ }
result=""
for para in $clean; do
    result=$result${para:0:1}
done
echo "${result^^}"


