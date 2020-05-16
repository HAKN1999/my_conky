#!/bin/bash

#dapatkan nama interface yang sedang aktif digunakan
ip r show|grep ' src '|cut -d ' ' -f 3,3 > ~/.conky/interface.txt

#tulis ulang di file interface.txt
while read -r line; do
	var="$line"
done < ~/.conky/interface.txt

#today
vnstat -i $var

#week
vnstat -i $var -w

#month
vnstat -i $var -m
