#!/usr/bin/python3
segment_size = 30
window_offset = 3

protein_coding_regions = open("remote_coding.fasta").read().split('1')[1]
#the above is silly but it's because i accidentally didn't have a line break
#between my header and my sequence oopsie
starting_base = 0
counter=0
with open('allsegments.fasta','w') as allfile:
	for i in range(segment_size):
		protein_coding_segment = protein_coding_regions[starting_base:segment_size-1+starting_base]
		print(f'This is segment number {i}. The starting base is {starting_base}')
		print(protein_coding_segment)
	#percentage GC content of each segment
		gc_proportion = (protein_coding_segment.count('G') + protein_coding_segment.count('C'))/len(protein_coding_segment)
		print(f'The proportion of GC content is {gc_proportion*100} %')
#Modify your Python script/programme to write out the individual segments in fasta format (i.e. with an informative fasta header) into individual fasta files.
		description = "AJ22335, segment starting from the base" + str(starting_base)
		fastaheader = ">" +  description
		with open(description+'.fasta', 'w') as outfile:
			outfile.write(fastaheader + '\n')
			outfile.write(protein_coding_segment+'\n')
		allfile.write(fastaheader+'\n'+protein_coding_segment+'\n')
		outfile.close()
		starting_base += window_offset	
		counter += 1
