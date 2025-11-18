#!/usr/bin/python

import os,shutil
import numpy as np
import matplotlib.pyplot as plt
ecoli = open("/localdisk/data/BPSM/Lecture19/ecoli.txt").read().replace('\n','')[0:100000]
window = 1000
at_5000 = []
at_100000 = []
at_all = []

for start in range(50000 - window):
	win = ecoli[start:start+window]
	at_5000.append(  (win.count('A')+win.count('T')) / window)

for start in range(100000 - window):
        win = ecoli[start:start+window]
        at_100000.append(  (win.count('A')+win.count('T')) / window)

for start in range(len(ecoli) - window):
        win = ecoli[start:start+window]
        at_all.append(  (win.count('A')+win.count('T')) / window)

plt.figure(figsize=(10,20))
plt.subplot(221)
plt.plot(at_5000,label="AT",linewidth=3)
plt.xlabel("Position on genome")
plt.ylabel("Fraction of AT content")
plt.title("AT content with 1k window")
plt.legend()
plt.savefig("AT_graph.png",transparent=True)
plt.show()

#question 2

window_size = input("What is the desired window size?")
at_gc = input("Do you want to analyze AT or GC content?").upper()
portion_one = int(input("What is the starting range for the portion of the base you want analyzed?"))
portion_two = int(input("What is the end range for the portion of the genome?")


#should have some error processing as well, some try, some whatever

def plot_AT_or_GC(window_size,at_gc,portion_one,portion_two):
	ecoli = open("/localdisk/data/BPSM/Lecture19/ecoli.txt").read().replace('\n','')
	ecoli_range = ecoli[portion_one-1:portion_two-1]
	base = []
	for start in range(len(ecoli_range)-window)):
		win = genome[start:start+win]		
		if at_gc == "AT":
			base.append(  (win.count('A')+win.count('T')) / window)
		elif at_gc == "GC":
			base.append((win.count('G')+win.count('C'))/window)
	plt.figure(figsize=(20,10))
	plt.xlabel('Position on genome')
	plt.ylabel(f'Proportion of {at_gc} content')
	plt.title(f'{at_gc} content, {window} size windows')
	plt.savefig("user_input.png", transparent=True)
	plt.show()
