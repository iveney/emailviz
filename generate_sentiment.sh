#!/bin/bash

# the first line of the CSV file is comment
NUM=`wc -l sample.dat | awk {'print $1'}`
NUM=`expr $NUM - 1`
echo 'sentiment'
for i in `seq 1 $NUM`;
do
	echo `expr $RANDOM % 3 + 1`
done

# to join the two files, use paste:
# paste -d ',' file1 file2