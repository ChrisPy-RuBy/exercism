declare -A aa
aa=([hello]=world [ab]=cd)

echo ${aa[hello]}
echo ${aa[x]}
