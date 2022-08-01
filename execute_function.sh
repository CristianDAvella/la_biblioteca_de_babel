# !/bin/bash
# This script do queries HTTP for activating the function Escritor.

queries=$1
count=0

echo "$queries executions:"
while [ $count -lt $queries ]
do
	echo "\n"
	curl https://escritor.azurewebsites.net/api/escritor	
	count=$(( count + 1 ))
done

