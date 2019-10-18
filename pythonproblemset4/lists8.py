#Write a new script to create a list with the following data ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']. Use a for loop to iterate through each element of this list and:
#Print out each element.
#Print out the length and the sequence, separated by a tab.

#Modify the script from #11 so that you also print out the number (postion in the list) of each sequence (i.e., "1\t4\tACGT\n")


dnaseqs = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
count = 0

for dnaseq in dnaseqs :
	print(count, '\t',len(dnaseq), '\t' ,dnaseq) #can't figure out how to add position without specifically counting 
	count+=1

