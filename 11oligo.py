#return Oligopeptide melting temp given number of AAs

def oligo(A,T,G,C):
	length = (A+T+G+C)
	if length <= 13:
		tm = (A+T)*2 + (G+C)*2
	else: tm = 64.9 +41*(G+C - 16.4)/(A+T+G+C)
	return tm
print(oligo(5,7,3,4))

