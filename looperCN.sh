#!/bin/bash

f_pre="box_01_step_"	#FILENAME PREFIX
f_suf=".pdb"		#FILENAME SUFFIX 

strt=30000		#START
stp=200000		#STOP
incr=20			#INCREMENT

out="cn_box_01.txt"

rm -rf $out		#Delete previous ouput

tot=0
num=0

for f in $(seq -f "%014g" $strt $incr $stp)
do
	fn="$f_pre$f$f_suf"
	hb=$(./cn.py $fn)
	num=$(calc $num + 1)
	tot=$(calc $tot + $hb)
	printf "%-10f%-5f\n" $num $hb >> $out
done

printf "TOT   : %f\n" $tot >> $out
printf "NUM   : %f\n" $num >> $out
printf "AVG   : %f\n" $(calc $tot / $num) >> $out
