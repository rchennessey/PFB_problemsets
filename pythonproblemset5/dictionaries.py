#write script to construct dictionary of fav things

import sys

favthings = { 'book' : 'Harry Potter' , 'song' : 'Sucker - JBs' , 'tree' : 'Maple'}

favthings['organism'] = 'dolphin'

favthing = input(favthings.keys())

print(favthings[favthing])

for things in favthings :
	value = favthings[things]
	print(things, value)

