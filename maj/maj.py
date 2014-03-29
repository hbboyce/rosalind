with open('rosalind_maj.txt') as f:		# read input
	# array to hold array elements
	arrs = []
	# read in k and n
	k, n = (int(x) for x in f.readline().split())
	# read in k arrays of size n
	for i in xrange(k):
		arrs.append([int(x) for x in f.readline().split()])

# string for output
out = ''

# nested for loop
for i in xrange(k):
	for j in xrange(n):
		# if a given item is a majority, add to output and break
		if arrs[i].count(arrs[i][j]) > (n / 2):
			out += str(arrs[i][j]) + ' '
			break;
		# if no majority add -1
		if j == (n-1):
			out += '-1 '
# print output
print out