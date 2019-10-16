#!/usr/bin/env python3

import sys  #need to import sys to use input from command line

name = sys.argv[1] #assigning name variable to the 1st input
color = sys.argv[2]
activity = sys.argv[3]
animal = sys.argv[4]

print('My name :', name+  '\n' # '\n' will add a line break, the + doesn't leave a space, a comma between print arguments will add a space
'My favorite color:', color+  '\n'
'My favorite activity:', activity+ '\n'
'My favorite animal:', animal)


