#!/usr/bin/python3

genomic_file = open('input.txt')
myfile_genomic = open("genomic_out.txt","w")
for line in genomic_file:
	line_wo_adapter = line[14:]
	line_length = len(line_wo_adapter.rstrip('\n'))
	myfile_genomic.write(line_wo_adapter)
	print(f'The line length is {line_length}')
