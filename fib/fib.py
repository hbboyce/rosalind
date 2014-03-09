# open file and set n to first value, k to second value
with open('rosalind_fib.txt') as f:
	for line in f:
		int_list = [int(i) for i in line.split()]
n = int_list[0]
k = int_list[1]

# iterative fibonacci function.
# Each value is (n-1) + ((n-2)*k)
def f(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, (a*k) + b
    return a

# print answer
print f(n)