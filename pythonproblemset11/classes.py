#Create a DNA sequence class that will contain a sequence, its name, and it's organism of origin. Do this by creating an __init__ function.

class DNArecord(object) : 
	def __init__(self, sequence, gene, organism):
		self.sequence = sequence
		self.gene = gene
		self.organism = organism
	
	def seqlength(self) :				#defining a method to determine seq length of the sequence
		length = len(str(self.sequence))  #converting to string here so i don't have to do it later in print statement
		return length

	def ntcontent(self) :   #definind method to determine nt content (# of each nt)
		aCount = self.sequence.count('A')
		tCount = self.sequence.count('T')
		cCount = self.sequence.count('C')
		gCount = self.sequence.count('G')
		ntcontent = 'A:', aCount, 'T:', tCount, 'C:', cCount, 'G:', gCount
		return ntcontent

	def gccontent(self) : #defining method for gccontent, needed to redefine length, c and g count under this method even though it is above in other methods.
		length = len(str(self.sequence))		
		cCount = self.sequence.count('C')
		gCount = self.sequence.count('G')
		gc_content = (cCount + gCount) / length
		return '{:%}'.format(gc_content)

	def format_dna(self):
		import re
		fastaformat = re.sub(r'(.{60})',r'\1\n',self.sequence)
		return fastaformat

#Write some some lines of code, outside your class (in your main program) that sets the name, DNA sequence, and organism for a gene.

dnarecord_1 = DNArecord('ATGCCCGTAGTCAGTCAGTGCTAGCTGACTAAGCTGGGAGATGATGATCCCCGTACGATCGATCGATCGATCGATCGATCGATCGATCGATCGCTCGATCATGCTAGCTAGGGATAGCTAGCTTTAGATCGATCGATCGCTAGGCTAATCGATCGATCGTAGCATTCG', 'Lol1', 'Mus musculus')

#Write some some lines of code, outside your class that:
	#a. uses the object sequence attribute to retrieve and print the sequence.
	#b. uses the object name attribute to retrieve and print the name.
	#c. uses the object organism attribute to retrieve and print the organism.

print('seq:', dnarecord_1.sequence, 'lenghth:',dnarecord_1.seqlength(), 'gene:', dnarecord_1.gene, 'organism:', dnarecord_1.organism)
print('Nucleotide Content:',dnarecord_1.ntcontent())
print('GC Content:', dnarecord_1.gccontent())
print(dnarecord_1.format_dna())

