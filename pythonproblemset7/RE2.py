#In the file Python_07_nobody.txt substitute every occurrence of 'Nobody' with your favorite name and write an output file with that person's name (ex. Michael.txt).

import re

with open("Python_07_nobody.txt", "r") as nobody, open("becky.txt", "w") as nobodyWrite : 
	for line in nobody:
		line = line.strip()
		beckyPoem = re.sub(r"Nobody","Becky", line)
		nobodyWrite.write(beckyPoem + '\n')
	
			



		  
