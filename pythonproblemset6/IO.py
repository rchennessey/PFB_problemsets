#Write a script to do the following to Python_06.txt
	#Open and read the contents.
	#Uppercase each line
	#Print each line to the STDOUT

with open("Python_06.txt","r") as pythonR, open("Python_06_uc.txt", "w") as pythonW :
	for line in pythonR :
		line = line.rstrip()
		lineUp= line.upper()
		pythonW.write(lineUp + '\n')
	

