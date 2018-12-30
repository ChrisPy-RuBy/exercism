error="Error: invalid input"
if [ $1 -gt 0 ] && [ $1 -lt 65 ]
then
    let power=$1-1
    python -c "x = 2**$power; print x"
else
    echo $error
    exit 1
fi
