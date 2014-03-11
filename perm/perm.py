# for permutation function
from itertools import permutations

# open file and read n
with open('rosalind_perm.txt') as f:
	n = int(f.readline().strip())

# to hold total permutations
total = 0
# to hold output
output = ''

# for loop going over number of permutations of n length
for item in permutations(range(1, n+1), n):
	# increment toal
	total += 1
	# write each permutation to perm and add it to a new line in output
	perm = ' '.join(str(item[i]) for i in range(n))
	output += '\n' + perm

# print total and output
print total, output