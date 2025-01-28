#return Oligopeptide length and melting temp given a number of AAs

def oligo(A,T,G,C):
	length = (A+T+G+C)
	print("Your oligopeptide length is", length)
	if length <= 13:
		tm = (A+T)*2 + (G+C)*2
	else: tm = 64.9 +41*(G+C - 16.4)/(A+T+G+C)
	return tm
print("Oligo1 melting temp:", oligo(5,7,3,4))
print("Oligo3 melting temp:", oligo(1,1,1,1))
print("Oligo3 melting temp:", oligo(24,24,17,17))