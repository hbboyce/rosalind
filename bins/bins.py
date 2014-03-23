def bins (arr, k):
	mini = 0
	maxi = len(arr) - 1
	while True:
		if maxi < mini:
			return -1
		i = (mini + maxi) / 2
		if arr[i] < k:
			mini = i + 1
		elif arr[i] > k:
			maxi = i - 1
		else:
			return i + 1

with open('rosalind_bins.txt') as f:
	n = int(f.readline().strip())
	m = int(f.readline().strip())
	a = [int(x) for x in f.readline().split()]
	k = [int(x) for x in f.readline().split()]

out = ''
for item in k:
	out += str(bins(a, item)) + ' '
print out