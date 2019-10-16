#! usr/bin/env python3

import sys

number = float(sys.argv[1]) #the input is considered a string but we want it to be a number so add in the float

if number > 0 :
	message = 'is greater than 0'
	print(number, message)
	if number < 50 and number%2 == 0 :
		print(number, 'is less than 50 and even')
	elif number > 50 and number%3 == 0 :
		print(number, 'is greater than 50 and divisible by 3')
elif number == 0 :
	message = 'is zero'
	print(number, message)
else :
	message = 'is negative'
	print(number, message)
