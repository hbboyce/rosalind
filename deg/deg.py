with open('rosalind_deg.txt') as f:		# open input file
	# list for degree sequence
	edges = []
	# read in n (num vertices) and m (num edges)
	n, m = (int(x) for x in f.readline().split())
	# read in each edge and place into list
	for i in xrange(m):
		e = f.readline().split()
		edges.append(int(e[0]))
		edges.append(int(e[1]))

# for each vertex count number of edges incident and print to screen
print " ".join(str(edges.count(x+1)) for x in xrange(n))