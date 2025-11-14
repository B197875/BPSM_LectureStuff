import re
gene_accession_numbers = ["xkn59438", "yhdck2", "chdsye847", "hedle3455", "xjhd53e", "45da", "de37dp"]
for accession in gene_accession_numbers:
	if re.search(r"5",accession):
		print(f"Accession {accession} contains the integer 5.")
	if re.search(r"[de]",accession):
		print(f"{accession} contains d or e")
	if re.search(r"de",accession):
		print(f"{accession} contains de")
	if re.search(r"d.e",accession):
		print(f"{accession} contains d and a with a letter between.")
	if re.search(r"d",accession) and re.search(r"e",accession):
		print(f"{accession} contains d and e in any order.")
	if re.search(r"^[xy]",accession):
		print(f"{accession} starts with x or y.")
	if re.search(r"^[xy]",accession) and re.search(r'e$',accession):
		print(f"{accession} starts with x or y and ends with e.")
	if len(re.findall("\d",accession))==3:
		print(f"{accession} has 3 digits in it.")
	if len(list(set(re.findall(r"\d",accession)))) == 3:
		print(f"{accession} has 3 unique digits in it.")
	if re.findall(r'\d{3,}',accession):
		print("{accession} has 3 or more digits in a row (i hope lol)")
	#end with d followed by either a, r or p
	if re.search(r"d[arp]$",accession):
		print("{accession} ends with d followed by a, r or p")
