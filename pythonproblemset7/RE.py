#In the file Python_07_nobody.txt find every occurrence of 'Nobody' and print out the position

import re
count = 0

with open("Python_07_nobody.txt", "r") as nobody : 
	for line in nobody:
		line = line.strip()
		for match in re.finditer(r"(Nobody)", line) :
			count +=1
			nobodies = match.group(1)
			start = match.start(1)
			end = match.end(1)
			print(nobodies, "line:", count, "start:", start, "end:", end, sep= ' ')
			



		  
