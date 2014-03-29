with open('rosalind_ins.txt') as f:		# read input
	# read n
	n = int(f.readline().strip())
	# read in array of n integers
	arr = [int(x) for x in f.readline().split()]

# var for output of total swaps in insertion sort
swaps = 0

# insert sort
for i in xrange(1, n):
	k = i
	while k >= 1 and arr[k] < arr[k-1]:
		arr[k], arr[k-1] = arr[k-1], arr[k]
		swaps += 1
		k -= 1
# print number of swaps
print swaps