#! usr/bin/env python3

number = 50

if number > 0 :
	print('positive')
	if number < 50 and number%2 == 0 :
		print('number is less than 50 and even')
	elif number > 50 and number%3 == 0 :
		print('number is greater than 50 and divisible by 3')
elif number == 0 :
	print('number is zero')
else :
	print('negative')

