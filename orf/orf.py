# list of stop codons
stop_codon = ['TAA', 'TAG', 'TGA']
# create codon_table and load codon_table.txt into it
codon_table = {}
with open('codon_table.txt') as f:
	for line in f:
		split = line.split()
		codon_table[split[0]] = split[1]

# read input data
with open('rosalind_orf.txt') as f:
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

# returns a list of indices with start codons
def FindStart(dna):
	starts = []
	for i in xrange(len(dna)-3):
		if dna[i:i+3] == 'ATG':
			starts.append(i)
	return starts

# Reads the dna and translates to amino acid sequence
def Reading(dna, start):
	out = ''
	n = start
	codon = 'ATG'
	n += 3
	while codon not in stop_codon:
		if n > (len(dna)-3):
			return ''
		out += codon_table[codon]
		codon = dna[n:n+3]
		n += 3
	return out

# get reverse complement of the dna strand
reverse = ReverseComplement(dna)

# start positions
starts_reverse = FindStart(reverse)
starts_forward = FindStart(dna)

# output list
output = []

# read each amino acid sequence for the dna strand and the reverse complement
for item in starts_forward:
	read = Reading(dna, item)
	if read == '':
		continue
	if read not in output:
		output.append(read)
for item in starts_reverse:
	read = Reading(reverse, item)
	if read == '':
		continue
	if read not in output:
		output.append(read)

# print the output
for item in output:
	print item
