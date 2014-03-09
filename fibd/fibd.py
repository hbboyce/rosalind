# open file and set n to first value, m to second value
with open('rosalind_fibd.txt') as f:
	for line in f:
		int_list = [int(i) for i in line.split()]
n = int_list[0]
m = int_list[1]

fib = [1]*n

def f(n):
	for i in xrange(2, n):
		fib[i] = fib[i-1] + fib[i-2]
		if i >= m:
			fib[i] -= fib[(i-m)-1]
	return fib[i]

print f(n)