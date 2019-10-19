#Using pattern matching, find all the header lines in Python_07.fasta. Note that the format for a header in a fasta file is a line that starts with a greater than symbol and is followed by some text (e.g. >seqName description where seqName is the sequence name or identifier. The identifier cannot have spaces in it. The description that follows it can have spaces.)

import re

with open("Python_07.fasta", 'r') as fasta :
	for line in fasta:
		line = line.strip()
		if re.search(r"(^>\S+)(.*)", line) :
			header = re.search(r"(^>\S+)(.*)", line)			
			seqName = header.group(1)
			desc = header.group(2)
			print('id:',seqName, 'desc:', desc)
			
