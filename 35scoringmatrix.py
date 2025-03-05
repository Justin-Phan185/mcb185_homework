import sys
nucs = (sys.argv[1])
mat = (sys.argv[2])
mis = (sys.argv[3])

print("  ", end="")
for nucT in nucs:
	print( f' {nucT}', end=' ')
print()
for nucB in nucs:
	print(nucB, end =' ')
	for nucT in nucs:
		if nucT == nucB:
			print(f'{mat} ', end = '') 
		else:
			print(f'{mis} ', end = '')
	print()
#python3 35scoringmatrix.py ACGT +1 -1		
'''
for i in range(0, len(list)):
	for j in range(X, len(list)):
X = 0: all combinations
X = i: half-matrix with diagonal
X = i+1: half-matrix without diagonal
'''
