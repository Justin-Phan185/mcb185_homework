import sys
import mcb185
import math

def entropy(win): 
	a = win.count('A') / len(win)
	c = win.count('C') / len(win)
	g = win.count('G') / len(win)
	t = win.count('T') / len(win)
	h = 0
	if a !=0: h += a*(math.log2(a))
	if c !=0: h += c*(math.log2(c))
	if g !=0: h += g*(math.log2(g))
	if t !=0: h += t*(math.log2(t))
	return -h

w = int(sys.argv[2])
entropy_thresh = float(sys.argv[3])
set_N = False

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	print(f">{defline[:70]}")
	mask = list(seq)
	for i in range(len(seq)-w +1):
		win = seq[i:i+w]
		if entropy(win) < entropy_thresh: 
			for j in range(i,i+w):
				mask[j] = 'N'
	print('>',defline, sep ='')
	mask = ''.join(mask)
	for i in range(0,len(mask),60):
		print(mask[i:i+60])
'''
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	 print(defline[:70])
	 masked_seq = list(seq)
	 for i in range(len(seq)- w + 1):
	 	window_seq = seq[i:i+w]
	 	entropy_win = entropy(window_seq)
	 	if entropy_win < entropy_thresh:
	 		masked_seq[i:i + w] = ['N'] * w
#	 print(''.join(masked_seq[i:i + 60]))
'''