# iterative fibonacci function
def fibo (n):
	a = 0
	b = 1
	for i in range(n):
		a, b = b, a + b
	return a

# read input
with open('rosalind_fibo.txt') as f:
	num = int(f.readline().strip())

#print output
print fibo (num)