# to make permutations of input to compare strings
from itertools import permutations

# comparison for dna strings
def compare (n, m):
	# if the entire strings are equal return false
	if n == m:
		return False
	return n[-3:] == m[:3]

# open input and place into dict entries
with open('rosalind_grph.txt') as f:
	dna_dict = {}
	header = ''
	for line in f:
		if line.startswith('>'):
			header = line.strip()[1:]
			dna_dict[header] = ''
		else:
			dna_dict[header] += line.strip()

# create permutations of dna_dict(key,value)
dna_compare = permutations(dna_dict, 2)

# print if compare returns true
for item in dna_compare:
	if  compare(dna_dict[item[0]], dna_dict[item[1]]):
		print item[0], item[1]