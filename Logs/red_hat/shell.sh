#!/bin/bash

echo "Hello Kevin, greating from cathy!"

echo Hello ; echo there

#$fileName="shell.sh"

echo $fileName

if [ -z $fileName ]; then
    echo "length of file name is 0"
fi

if [ -x $fileName ]; then 
    echo "$fileName exists"
else
	echo "$fileName does not exist"
fi


variabel='a'
echo "\$variabel value is :" $variabel
case $vvariabel in
	a) echo "your input is a";; 
	b) echo "your selection is b";;
esac 
	
let "t2=((a=9, 15/3))"
echo $a
echo $t2

exit 0 
