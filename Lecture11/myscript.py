short_DNA = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
adenine_count = short_DNA.count("A")
print(f"Adenine count is {adenine_count}")
t_count = short_DNA.count("T")
print(f"Thymine count is {t_count}")
number = (adenine_count + t_count)/len(short_DNA)
print(number) 

new_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
complement_a = new_dna.replace("A","t")
complement_b = complement_a.replace("T","a")
complement_c = complement_b.replace("G","c")
complement_d = complement_c.replace("C","g")
complement = complement_d.upper()
print(complement)

DNA_three = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
motif = "GAATTC"
#I'm going to find the position of the motif. Then this gives me the 
# beginnings of this motif. that index + 1 is the position of the break
#since the break happens at G*AATC
motif_place = DNA_three.find(motif)
print(motif_place)
cut_place = motif_place+1
print(cut_place)
firstpart = DNA_three[0:cut_place]
secondpart = DNA_three[cut_place:]
len(secondpart)
print(len(secondpart))

genomic_dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
first_exon = genomic_dna[:62]
second_exon=genomic_dna[90:]
coding_dna = first_exon + second_exon
print(coding_dna)
percentage_coding = len(coding_dna)/len(genomic_dna)*100
print(f"Proportion coding is {percentage_coding}")

#Write a program that will print out the original genomic DNA sequence with coding bases in uppercase and non-coding bases in lowercase.

introns = genomic_dna[63:89]
introns.lower()
total = first_exon + introns.lower() + second_exon
print(total)

