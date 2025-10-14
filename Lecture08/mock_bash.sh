#!/bin/bash
counter=0;
rm singleline_NCBIseqs.fasta
while read line
do
[ -z "${line}" ] && continue
if test ${line:0:1} == ">"
counter=$((${counter}+1))
if test ${counter} == 1
then
printf "\n"${line}"\n" >> singleline_NCBIseqs.fasta
else
printf ${line}"\n" >> singleline_NCBIseqs.fasta
fi
else
printf ${line} >> singleline_NCBIseqs.fasta
fi
done < mock_NCBI.fasta

