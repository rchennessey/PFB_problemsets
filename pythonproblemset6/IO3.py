#Open the FASTQ file Python_06.fastq and go through each line of the file. Count the number of lines and the number of characters per line. Have your program report the:
	#total number of lines
	#total number of characters
	#average line length

linecount = 0
linechar = 0

with open("Python_06.fastq", "r") as pythonfastq :

	for line in pythonfastq :
		line = line.rstrip()
		linecount+=1
		charsperline = len(line)
		linechar += charsperline
print("total number of lines:", linecount)
print("total number of characters:", linechar)
print("average line length:", linechar/linecount)

