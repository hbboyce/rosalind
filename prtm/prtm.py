# dict to hold amino acids with their respective masses
mass_table = {}
# open masstable.txt and read in amino acids with masses into dict
with open('masstable.txt') as f:
	for line in f:
		split = line.strip().split()
		mass_table[split[0]] = float(split[1])

# initialize mass
mass = 0.0
# open input and sum masses of amino acids
with open('rosalind_prtm.txt') as f:
	for line in f:
		for i in xrange(len(line)-1):
			mass += mass_table[line[i]]

# print mass
print mass