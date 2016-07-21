#!/bin/bash
for file in $(pwd)/*
do
	echo $file	
	astyle -s3 -b -S -Y -f -p -H -y -k2 -n -v -z2 "$file"
done

