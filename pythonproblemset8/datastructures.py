#Take a multi-FASTA Python_08.fasta file from user input and calculate the nucleotide composition for each sequence. Use a datastructure to keep count. Print out each sequence name and its compostion in this format seqName\tA_count\tT_count\tG_count\C_count

import re

seqId = ''
fastadict = {}


with open("smallPython_08.fasta", "r") as smalltest :
	for line in smalltest :
		line = line.rstrip()
		if line.startswith('>') :  # to create a fasta parser, presave an empty dictionary, find header lines with if statement
			for header in re.finditer(r'(^>\S+)\s+(.*)', line) : #using RE to find the fasta header and able to save the gene id and any description
				seqId = header.group(1) #saving only the gene id portion of the header; can also save the description if we needed it
				fastadict[seqId] = ''
		else : #this is for all the actual seq lines
			fastadict[seqId] += line #here we are writing the seqId as the key and the seq to a premade dictionary, this will rewrite every loop to add on to the seq until next header
#print(fastadict)

genenuc = {}

for seqId in fastadict :
	print(seqId)
	genenuc[seqId] = {}
	countA = fastadict[seqId].count('A')
	genenuc[seqId]['A'] = countA
	countT = fastadict[seqId].count('T')
	genenuc[seqId]['T'] = countT
	countG = fastadict[seqId].count('G')
	genenuc[seqId]['G'] = countG
	countC = fastadict[seqId].count('C') 	
	genenuc[seqId]['C'] = countC
	#print(seqId,countA,countT,countG,countC)

print(genenuc)


	
		
