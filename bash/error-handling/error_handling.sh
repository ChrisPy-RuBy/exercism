#!/usr/bin/env bash
#set -u
#set -x

main () {
if [[ $# == 0 ]]; then
    echo "Usage: ./error_handling <greetee>"
    exit 1
elif [[ $# -ne 1 ]]; then
    exit 1
else
    echo "Hello, $1"
fi
}

main "$@"
