# for cartesian product
from itertools import product
# read input
with open('rosalind_lexf.txt') as f:
	alphabet = f.readline().strip().split()
	n = int(f.readline().strip())

# produce product of all n length items in alphabet
lexicograph = product(alphabet, repeat=n)
# print each item in lexicograph
for item in lexicograph:
	out = ''
	for i in xrange(n):
		out += item[i]
	print out