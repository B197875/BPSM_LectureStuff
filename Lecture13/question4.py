#!/usr/bin/python3	

#Write a Python script/programme which creates nine new 'size range' directories, one for sequences between 100 and 199 bases long, one for sequences between 200 and 299 bases long, etc., etc..

import os, subprocess, shutil

for bin_lower in list(range(0,1000, 100)):
        bin_upper = bin_lower + 99
        bin_dir_name = str(bin_lower) + '_to_' + str(bin_upper)
        shutil.rmtree(bin_directory_name)
        os.mkdir(bin_dir_name)
for file_name in os.listdir('dna_files') : 
# Check if the file name ends with .dna
  if file_name.endswith('.dna') : 
    print('Reading sequences from ' + file_name) 
# Open the file and process each line
    dna_file = open('dna_files/' + file_name) 
    for line in dna_file :
# Calculate the sequence length 
      dna = line.rstrip('\n') 
      length = len(dna) 
      print('\tsequence length is ' + str(length))
# Go through each size bin and check if the sequence belongs in it
      for bin_lower in list(range(100,1000,100)) : 
        bin_upper = bin_lower + 99 
        if length >= bin_lower and length <= bin_upper : 
          print('\t\tbin is ' + str(bin_lower) + ' to ' + str(bin_upper)) 
          bin_directory_name = str(bin_lower) + '_' + str(bin_upper) 
          output_path = bin_directory_name + '/' + str(seq_number) + '.dna' 
          output = open(output_path, 'w') 
          output.write(dna) 
          output.close(
sequence_number = 1
for file in os.listdir('dna_files/'):
	if file.endswith('.dna'):
		print(f'Reading from {file}')
		dna_file = open('dna_files/' + file)
		for line in dna_file:
			line_stripped = line.rstrip('\n')
			length_seq = len(line_stripped)
			print(f'Line length of this sequence is {length_seq}')
			for bin_lower in list(range(0,1000,100):
				bin_upper = bin_lower + 99
				if length_seq >= bin_lower and length_seq <= bin_upper:
					bin_dir_name = str(bin_lower) + '_to_' + str(bin_upper)
					output_path = bin_dir_name + '/' + str(seq_number) + '.dna'
					sequence_number += 1
					dna_open = open(output_path, 'w')
					dna_open.write(line)
					dna_open.close()

				
#how would i go about making size bins? 
#deffo would use range. maybe loop through between 0 and 1000 and make bins of size
#0-99, 100-199, 200-299, etc. for each of these, we make a directory
#and then copy it into it?

for bin_lower in list(range(0,1000, 100)):
	bin_upper = bin_lower + 99
	bin_dir_name = str(bin_lower) + '_to_' + str(bin_upper)
	shutil.rmtree(bin_directory_name)
	os.mkdir(bin_dir_name)
	
