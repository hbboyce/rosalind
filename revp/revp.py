# read input
with open('rosalind_revp.txt') as f:
	f.readline()
	dna = ''
	for line in f:
		dna += line.strip()

# returns complement of a given nucleotide
def Complement(nuc):
	if nuc == 'A':
		return 'T'
	elif nuc == 'T':
		return 'A'
	elif nuc == 'C':
		return 'G'
	elif nuc == 'G':
		return 'C'

# returns ReverseComplement of dna strand
def ReverseComplement(dna):
	comp = ''
	for i in xrange(len(dna)):
		comp += Complement(dna[i])
	return comp[::-1]

# at each position in the strand compare substrings of 
# length 4-12 to it's reverse complement
for i in xrange(len(dna)-3):
	for j in xrange(4,13):
		# if i+j is greater than len(dna) continue to next iteration
		if i+j > len(dna):
			continue
		# assign dna substring and compare printing the index and 
		# substring length if it is a hit
		test = dna[i:i+j]
		if test == ReverseComplement(test):
			print i+1, j