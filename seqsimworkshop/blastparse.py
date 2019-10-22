#

import sys

hit_files =[]

fields =['qseqid', 'sseqid', 'percid', 'alen', 'mismat', 'gaps', 'q_start', 'q_end', 's_start' , 's_end', 'evalue', 'bits']

hits_list =[]

for hit_file in sys.argv[1:] : 
	with open (hit_file, "r") as input :
		for line in input :
			line = line.rstrip()
			if line.startswith('#'):
				continue
			else :
				hit_data = dict(zip(fields, line.split('\t')))
				hit_data['file'] = hit_file
				hits_list.append(hit_data)
				break

for hit in hits_list:
	print('\t'.join([hit[x] for x in ('file', 'percid', 'alen', 'evalue')]))
		
