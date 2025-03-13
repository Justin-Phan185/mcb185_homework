import sys
import mcb185
import sequence

w = int(sys.argv[2])

for defline, seq in mcb185.read_fasta(sys.argv[1]):		
	for i in range(len(seq) -w +1):
		s = seq[i:i+w]
		print(i, sequence.gc_comp(s), sequence.gc_skew(s))
	
