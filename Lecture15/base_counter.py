#!/usr/bin/python

def base_counter(dna_sequence, threshold=None):
	counter = 0
	for base in dna_sequence:
		if base not in ['A','T','C','G']:
			counter += 1
	if counter/len(dna_sequence) > int(threshold):
		return False
	else:
		 return True

assert base_counter("ABCD",threshold=0) == False
assert base_counter("ATCG", threshold=1) == False
