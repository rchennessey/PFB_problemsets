#Write a python program that reads in the 'bowtie2.sam' file and generates a table containing the number of reads mapped to each gene.

import sys
import re

genetranscriptdict = {}

with open(sys.argv[1]) as samfile :
	for line in samfile :
		line = line.rstrip()
		splitline = line.split('\t')
		readname = splitline[0]
		transcriptseq = re.search(r"(.*)\^.*", splitline[2])
		genename = transcriptseq.group(1)
		if genename not in genetranscriptdict :
			genetranscriptdict[genename] = set()
		else :
			genetranscriptdict[genename].add(readname)

#created a dictionary with gene name and then the value is a set of all the transcript ids associated with that gene

	genes = list(genetranscriptdict.keys())

	genes = sorted(genes, key=lambda x: len(genetranscriptdict[x]), reverse = True)

	for gene in genes:
		read_set = genetranscriptdict[gene]
		print("{}\t{}".format(gene, len(read_set)))

