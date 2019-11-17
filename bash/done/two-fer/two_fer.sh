#!/usr/bin/env bash

# default input parameter syntax
# more information on this can be found 
# https://stackoverflow.com/questions/9332802/how-to-write-a-bash-script-that-takes-optional-input-arguments
# and
# https://www.gnu.org/software/bash/manual/bashref.html#Shell-Parameter-Expansion
var=${1-you}

echo "One for $var, one for me."
