#Iterate through each element of this list using a for loop: [101,2,15,22,95,33,2,27,72,15,52]
#Print out only the values that are even (hint: use the modulus operator).

numlist =sorted([101,2,15,22,95,33,2,27,72,15,52])
evennum = 0
oddnum = 0

for num in numlist:
	if num%2 == 0 :
		evennum += num		
	else :
		oddnum += num
print('Sum of even numbers:', evennum)
print('Sume of odd numbers:', oddnum)
