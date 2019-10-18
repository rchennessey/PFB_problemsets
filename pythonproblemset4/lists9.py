#Use list comprehension to generate a list of tuples. The tuples should contain sequences and lengths from the previous problem. Print out the length and the sequence (i.e., "4\tATGC\n"). A list of tuples looks like this [(4,'ATGC'),(2,'GC')].


dnaseqs = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

listoftuples = [(len(dnaseq), dnaseq) for dnaseq in dnaseqs] #couldn't figure out how to put the /t into the tuple portion (len(dnaseq), dnaseq) without getting an error at the end of the line

print(listoftuples)
