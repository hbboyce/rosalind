import operator		# for iterating over nucleotide counts to find max

dna = []			# list to hold dna strings from input file
dna_string = ''

# for final output
outdna = ''
a_out = 'A:'
c_out = 'C:'
g_out = 'G:'
t_out = 'T:'

# open input to get list of dna strings
with open('rosalind_cons.txt') as f:
	f.readline()
	for line in f:
		if line.startswith('>'):
			dna.append(dna_string)
			dna_string = ''
		else:
			dna_string += line.strip()
	dna.append(dna_string)
	
# get the length of the dna strings and create
# lists for each nucleotide of that length
k = len(dna[0])
a_count = [0] * k
c_count = [0] * k
g_count = [0] * k
t_count = [0] * k

# iterate over each dna string and count the number of times
# each nucleotide appears in each location
for item in dna:
	a, c, g, t = 0, 0, 0, 0
	for i in range(len(item)):
		if item[i] == 'A':
			a_count[i] += 1
		elif item[i] == 'C':
			c_count[i] += 1
		elif item[i] == 'G':
			g_count[i] += 1
		elif item[i] == 'T':
			t_count[i] += 1

# iterate over the length of the dna string to do multiple things
# as described individually below
for i in range(k):
	# find max count nucleotide in each position and add to the output string
	nuc_dict = {'A':a_count[i], 'C':c_count[i], 'G':g_count[i], 'T':t_count[i]}
	outdna += max(nuc_dict.iteritems(), key=operator.itemgetter(1))[0]

	# build up individual nucleotide outputs
	a_out += ' ' + str(a_count[i])
	c_out += ' ' + str(c_count[i])
	g_out += ' ' + str(g_count[i])
	t_out += ' ' + str(t_count[i])

# print output
print outdna
print a_out
print c_out
print g_out
print t_out
