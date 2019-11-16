#!/usri/bin/env bash
for param in ${*:2:4}; do
    if (( $(echo "$param == 0" | bc -l))); then
        echo "false"; exit 0
    fi
done

if [[ -z $1 ]]; then
    triangle="**Unknown triangle**"
elif [[ -n $1 ]]; then
    triangle=$1
fi


count_sides () {
    counter=0
    if (( $(echo "$3 == $2" | bc -l ))); then
        ((counter++))
    fi
    if (( $(echo "$3 == $4" | bc -l ))); then
        ((counter++))
    fi
    if (( $(echo "$2 == $4" | bc -l ))); then
        ((counter ++))
    fi
    echo "$counter"
}

check_inequality () {
    if (( $(echo "$2 + $3 < $4" | bc -l )))  ||
       (( $(echo "$3 + $4 < $2" | bc -l ) )) ||
       (( $(echo "$2 + $4 < $3" | bc -l ) )); then
         echo false; exit 0
    fi
}




check_inequality "$@"

case $triangle in
    "equilateral")
        if [[ $(count_sides "$@") -eq 3 ]]; then
            echo true
        else
            echo false; fi;;
    "isosceles")
        if [[ $(count_sides "$@") -ge 1 ]]; then
            echo true
        else
            echo false; fi;;
    "scalene")
        if [[ $(count_sides "$@") -eq 0 ]]; then
            echo true
        else
            echo false; fi;;
    *) echo "false"
esac

