# open input and assign data to protein
with open('rosalind_mrna.txt') as f:
	protein = f.readline().strip()

# lists of any codons with more than 1 encoding codon
# (all but M and W)
six_codon = ['L', 'R', 'S']
four_codon = ['V', 'P', 'T', 'A', 'G']
three_codon = ['I']
two_codon = ['F', 'Y', 'H', 'Q', 'N', 'K', 'D', 'E', 'C']

# to multiply output
out = 1
# modulus
mod = 1000000

# multiply out by number of encoding codons for a given amino acid
for i in protein:
	if i in six_codon:
		out *= 6
	elif i in four_codon:
		out *= 4
	elif i in three_codon:
		out *= 3
	elif i in two_codon:
		out *= 2
	else:
		continue

# print out * 3 (for 3 stop codons) and % by mod
print (out*3) % mod