#!/usr/bin/env python

import os, sys



## method: seq_list_from_fastq_file(fastq_filename)
##
##  Extracts the sequence lines from a fastq file and returns a list
##  of the sequence lines
##
##  input parameters:
##
##  fastq_filename :  name of the fastq file (type: string)
##
##  returns seq_list : list of read sequences.
##                    ie.  ["GATCGCATAG", "CGATGCAG", ...]
    
def seq_list_from_fastq_file(fastq_filename):
	seq_list = list()
	fh = open(fastq_filename)
	counter=0
	for line in fh: #here is setting a counter to count the number of lines, then using the modulus operater % to determine the 2nd line out of of every 4 lines (fastq file set up) (aka 1%4 = 1, 2%4 = 2, 3%4 = 3, 4%4 = 0 ... so to get the 2nd line set the counter%4 == 2)
		line = line.rstrip()
		counter += 1
		if counter%4 == 2 :
			seq_list.append(line)	
    ## end your code
	return seq_list



def main():

    progname = sys.argv[0]
    
    usage = "\n\n\tusage: {} filename.fastq num_seqs_show\n\n\n".format(progname)
    
    if len(sys.argv) < 3:
        sys.stderr.write(usage)
        sys.exit(1)

    # capture command-line arguments
    fastq_filename = sys.argv[1]
    num_seqs_show = int(sys.argv[2])

    seq_list = seq_list_from_fastq_file(fastq_filename)

    print(seq_list[0:num_seqs_show])

    sys.exit(0)  # always good practice to indicate worked ok!



if __name__ == '__main__':
    main()
    
