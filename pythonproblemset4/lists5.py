#Write a script that uses range() in a for loop to print out every number between 0 and 99
#Modify your loop to print out every number between 1 and 100.

for num in range(101):
	if num == 0:  #don't want to print 0 so add the continue to skip the print only if num = 0
		continue
	print(num)

