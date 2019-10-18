#Open and print the reverse complement of each sequence in Python_06.seq.txt. Each line is the following format: seqName\tsequence\n. Make sure to print the output in fasta format including the sequence name and a note in the description that this is the reverse complement. Print to STDOUT and capture the output into a file with a command line redirect '>'.

sequences ={}

with open("Python_06.seq.txt", "r") as pythonseq :
	for line in pythonseq : 
		line = line.rstrip()  #removing white space at end of line
		seqName,seq = line.split('\t') # splitting line at tab to get sequence name and seq seperately
		seqLow = seq.lower() #to reverse complement need to lowercase every sequence and perform the complement as below
		aTswitch = seqLow.replace('a', 'T')
		tAswitch = aTswitch.replace('t', 'A')
		gCswitch = tAswitch.replace('g', 'C')
		dna_comp = gCswitch.replace('c', 'G')
		dna_revcomp = dna_comp[::-1]  #reverse of the complement

		sequences[seqName] = dna_revcomp #making the dictionary with seq names and reverse complemented sequences
	
for seqName in sequences : #getting contents of dict into a string to print as a fasta file format
	print('>'+ seqName+' | Reverse Complement'+'\n'+sequences[seqName])
