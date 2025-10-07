#!/bin/bash
unset IFS
IFS=$'\t'
while read name email city birthday_day birthday_month birthday_year country
do
if test -z ${name} ||test -z ${country} || test ${country} == "country"
then
continue
else
echo -e "${name}\t$city\t${country}" >> ${country// /}.data
fi
done < example_people_data.tsv
