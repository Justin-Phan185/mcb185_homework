import math

def symbol_to_prob(c):
	pqv = ord(c) - 33
	prob = 10**(-pqv/10)
	return prob


def prob_to_letter(d):
	pqv = -10 * math.log10(d)
	letter =  chr(int(pqv)+33)
	return letter
	
print(symbol_to_prob("9"))
print(prob_to_letter(0.003981071705534973))
print(symbol_to_prob("8"))
print(prob_to_letter(0.005011872336272725))
print(symbol_to_prob("J"))
print(prob_to_letter(0.00007943282347242822))
print(symbol_to_prob("j"))
print(prob_to_letter(0.00000005011872336272725))
'''
math.log10
math.log2
math.log  #will be log e

print(ord('A'))
print(ord('B'))
print(ord('Z'))
print(ord('a'))

print('1')
print('2')

print(chr(55))
print(chr(56))
print(chr(57))
print(chr(60))
print(chr(61))
print(chr(62))

print(10**-3.2)
'''
'''
@mysecquencename
TYUI
+
A7,>

65 - 33 = 32 --->10**-3.2


#Convert these kinds of letters in to probailities
 #Or given a snumber and go backwards into it's corresponding sumbol
 
c = "k"
pqv = ord(c) - 33
print(pqv)

 
 
'''