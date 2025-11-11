#!/usr/bin/python

def amino_percentages(protein_seq, residue_code):
	count = 0
	for base in protein_seq:
		if base.upper() == residue_code.upper():
			count = count+1
			print(protein_seq)
	percentage = 100*count/len(protein_seq)
	print(percentage)
	return percentage

amino_percentages("MS","M")

assert round(amino_percentages("MSRSLLLRFLLFLLLLPPLP", "M")) == round(5)
assert round(amino_percentages("MSRSLLLRFLLFLLLLPPLP", "r")) == round(10)

#Amino acid percentages, part two:

def amino_percentages_listversion(protein_seq, residue_code=["A","L","I","M","F","W","Y","V"]):
	count = 0
        for base in protein_seq:
		for residue in residue_code:
	        	if base.upper() == residue.upper():
                       		count = count+1
        percentage = 100*count/len(protein_seq)
        return percentage

assert round(amino_percentages_listversion("MSRSLLLRFLLFLLLLPPLP", ["M"])) == 5
assert round(amino_percentages_listversion("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L'])) == 70
assert round(amino_percentages_listversion("MSRSLLLRFLLFLLLLPPLP")) == 65
