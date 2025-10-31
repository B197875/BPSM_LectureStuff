#!/usr/bin/python3
import os, shutil
shutil.copy("/localdisk/data/BPSM/Lecture13/genomic_dna2.txt", "genomic_dna2.txt")
shutil.copy("/localdisk/data/BPSM/Lecture13/exons.txt", "exons.txt")
exons = open("exons.txt")
outfile = open("outfileq2.txt","w")
genomic_2 = open("genomic_dna2.txt").read().rstrip('/n')
genomic_exons_list = []
for line in exons:
#	genomic_exon_first = int(line[0])
#	genomic_exon_second = int(line[1])
#	genomic_exon = genomic_2[genomic_exon_first:genomic_exon_second]
#actually we dont wanna do the above, bcs we can ahev a number that has
#more places so it's not just the second position in the string. so we
#want ti separated by the comma
	line = line.rstrip('\n')
	exon_list = line.split(',')
	first = int(exon_list[0])-1
	second = int(exon_list[1])
	genomic_exons = genomic_2[first:second]
	genomic_exons_list.append(genomic_exons)
print(genomic_exons_list)
s=','
new_string = s.join(str(e) for e in genomic_exons_list)
print(new_string)
final = new_string.replace(",","")

outfile.write(str(final))
outfile.close()
