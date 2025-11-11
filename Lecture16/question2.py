#!/usr/bin/python

gencode = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

import os

input_dna = input("What is the dna to be translated today?").upper()

#def read_trimers(input_dna, start):
#	amino_acid_list = []
#	for i in range(len(input_dna)):
#		start_codon = i+start #assuming start is given as starting at 0, and range starts at 0
#		trimer = input_dna[start_codon:start_codon+3]
#		if len(trimer) > 2
#			amino_acid_list.append(gencode[trimer])
#	return print(amino_acid_list)


#realized the above was a sliding window rather than reading them three by three!!

def read_trimers(input_dna, start):
	amino_acids_list = []
	count = 0
	trimer = ""
	for i in input_dna:
		if count > 3:
			trimer = ""
			count = 0
		elif count < 3:
			trimer += i
			count += 1
		elif count == 3:
			amino_acid = gencode[trimer]
			amino_acids_list.append(amino_acid)
			count += 1
	return print(amino_acids_list)


def read_trimers_fr(dna_input,start_codon):
	last_codon = len(dna_input) - 2
	list_translated = []
	for start in list(range(start_codon, last_codon, 3)):
		dna_upper = dna_input.upper()
		trimer = dna_upper[start:start+3]
		print(trimer)
		
		translated_aa = gencode[trimer]
		list_translated.append(translated_aa)
	print(list_translated)
read_trimers_fr(input_dna,0)

#now we have an actually working funtion for reading this in blocks of trimers, we want to:
#1. add an error message if there's a non-dna section?
#2. make another function that loops through start codongs 1-3
#and translates it from all 3 codons
#3. make a function that reverses it and then goes from -1 to -3

