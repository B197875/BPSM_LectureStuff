#!/usr/bin/python

def kmer_counting(dna, kmersize, minfrequency, offset):
	kmers = []
	for i in range(0,len(dna),offset):
		kmer = dna[i:i+kmersize]
		kmers.append(kmer)
	no_duplicates = list(set(kmers))
	for seq in no_duplicates:
		kmer_count = kmers.count(seq)
		if kmer_count > minfrequency:
			print(seq)

#ßkmer_counting("AATCGCTGAATGAATCTGAA", 2, 2, 1)
kmer_counting("AATCGCTAATGAATCTGAA", 2, 3, 1)  	

#second function, with user input, outputting a list

import os

input_dna = input("What is the DNA to be analyzed?").upper()
input_kmersize = int(input("What is the kmersize?"))
input_minfreq = int(input("What is the threshold frequency for kmers to be found?"))
def kmer_counting_withinput(dna=input_dna, kmersize=input_kmersize, minfrequency=input_minfreq, offset=1):
	kmers = []
	more_than_thresholdkmers = []
	for i in range(0,len(dna),offset):
                kmer = dna[i:i+kmersize]
                kmers.append(kmer)
	no_duplicates = list(set(kmers))
	for seq in no_duplicates:
	        kmer_count = kmers.count(seq)
	        if kmer_count > minfrequency:
	                print(seq)
			more_than_thresholdkmers.append(seq)
	return more_than_thresholdkmers

output = kmer_counting_withinput(dna=input_dna, kmersize=input_kmersize, minfrequency=input_minfreq, offset=1)
myfilename = "kmer of size_" + str(kmersize) + "minimum" + str(input_minfreq)
myfilepipe = open(myfilename, "w")


