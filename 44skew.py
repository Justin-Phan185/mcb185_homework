import sys
import mcb185
import sequence

w = int(sys.argv[2])
g = 0
c = 0

for defline, seq in mcb185.read_fasta(sys.argv[1]):	
	g = seq[:w].count('G')
	c = seq[:w].count('C')	
print('0',sequence.gc_comp(seq[:w]), sequence.gc_skew(seq[:w]))

for i in range(1,len(seq) -w +1):
	if seq[i-1] == 'G':
		g -=1
	elif seq[i-1] == 'C':
		c -=1
	if seq[i+w-1] == 'G':
		g += 1
	elif seq[i+w-1] == 'C':
		c += 1
	print( i,(g+c)/w, (g - c) / (g + c))
