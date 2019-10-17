#Write a new script that prints out the reverse complement of the above DNA string. Hint for reverse. Use string formating for printing.

dna = 'GATGGGATTggggttttccccTCCCATGTGCTCAAGACTGGCGCTaaaaGttttGAGCTTCTCaaaaGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCggggACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGccccCTCTGAGTCAGGAAACAttttCAGACCTATGGAAACTACTTCCTGaaaaCAACGTTCTGTccccCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTccccGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTccccCCGTGGccccTGCACCAGCAGCTCCTACACCGGCGGccccTGCACCAGccccCTCCTGGccccTGTCATCTTCTGTCCCTTCCCAGaaaaCCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTccccTGCCCTCAACAAGATGttttGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACAccccCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGccccCACCATGAGCGCT'

dna_upper = dna.upper() #convert to all uppercase for final formating later
dna_lower = dna.lower() #convert to all lowercase

#to get complement have set everything to lowercase so first change a to T and then t to A (able to tell the difference between what was new T and old T this way); repeat for G and C
aTswitch = dna_lower.replace('a', 'T') 
tAswitch = aTswitch.replace('t', 'A')
gCswitch = tAswitch.replace('g', 'C')
dna_comp = gCswitch.replace('c', 'G')

#reverse of the complement 
dna_revcomp = dna_comp[::-1]

#formatting

print("{:<20} 5'{} 3'".format("Original Sequence", dna_upper))
print("{:<20} 3'{} 5'".format("Complement", dna_comp))
print("{:<20} 5'{} 3'".format("Reverse Complement", dna_revcomp))


