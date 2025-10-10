#!/bin/bash
unset IFS
IFS=$'\t'
inputfile="$PWD/HPS_lines_only.ou"
HSP_counter=0
num_short_HSPs=0
while read -r line <<< ${inputfile}
do
while read q_ver s_ver percent_identity alignment_length mismatches \
gap_opens q_start q_end s_start s_end evalue bit_score 
do
echo -e "${q_Ver}\t${s_ver}" >> accessions.txt
echo -e "${alignment_lengt}\t${percent_identity}" >> alignment_n_percent.txt
if test ${mismatches} -gt 20
then
echo -e "${line}\t has more than 20 mismatches: \t${mismatches}"
fi
if test ${mismatches} -gt 20 && test ${alignment_length} -lt 100
do
echo -e "${line}\t has more than 20 mismatches and a lenght smaller than \
100 amino acids:\t${mismatches}\t${alignment_length}"
fi
if test ${mismatches} -lt 20
do
HP_counter = $((counter+1))
if test ${HP_counter} -lt 20
do
echo -e "${line}\t has more than 20 mismatches:\t${mismatches}"
fi
fi
if test {$alignment_length} -lt 100
do
num_short_HSPs = ((num_short_HSPs+1))
echo -e "${num_short_HSPs}"
fi

fi


