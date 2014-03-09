# open file and set k to first value, n to second value
with open('rosalind_lia.txt') as f:
	for line in f:
		int_list = [int(i) for i in line.split()]
k = int_list[0]
n = int_list[1]

# iterative factorial funtion
def fact(n):
	prod = 1
	for i in range(n):
		prod *= (i + 1)
	return prod

# m choose j function
def comb(m, j):
	return (fact(m) / (fact(j)*fact(m-j)))

# binomial distribution function n = gen, k = off, p = 0.25
# return the prob of k successes in n trials with probability p
def binom (gen, off):
	return comb(gen, off) * (0.25**off) * (0.75**(gen-off))

# number of offspring in kth generation
k_gen = 2**k

# set intial probability to 0
prob = 0.0
i = n

# sum Binom(k_gen, i) from i = n to k_gen
while i <= k_gen:
	prob += binom(k_gen, i)
	i += 1

# output probability
print prob