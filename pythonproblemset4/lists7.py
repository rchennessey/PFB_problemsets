#Write a new script that takes the start and end values from the command line. If you call your script like this count.py 3 10 it will print the numbers from 3 to 10.
#Modify your script so that it will only print the number if it is odd.

import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

while num1 < num2+1 :
	if num1%2 == 1 :
		print(num1)
	num1+= 1

