import urllib2
import re
# url prefix
url = "http://www.uniprot.org/uniprot/"
# regex motif to search for
motif = re.compile(r'(?=(N[^P][ST][^P]))')

# open file iteratre over each protein in the file
with open('rosalind_mprt.txt') as f:
	for line in f:
		uniprot_id = line.strip()
		uniprot = uniprot_id + '.fasta'
		# create an object for the .fasta file and assign to protein
		protein = urllib2.urlopen(url + uniprot)

		# string for the full protein sequence
		sequence = ''
		# string for locations for hits
		local = ''
		# build sequence from protein object
		for line in protein:
			if line.startswith('>'):
				continue
			else:
				sequence += line.strip()

		# create a list of motif hits in sequence
		local_list = [(m.start() + 1)for m in re.finditer(motif, sequence)]
		# build local string
		for item in local_list:
			local += str(item) + ' '

		if local == '': 	# if no hits skip to next protein
			continue	
		else:		# else print protein name and location of hits
			print uniprot_id
			print local