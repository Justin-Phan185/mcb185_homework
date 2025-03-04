'''
s = 'hello world'
print(s)

s1 = 'hey "dude"'
s2 = "wow that\'s crazy" #use of a delimiter
print(s1,s2, sep = ' ')

print(len('wow'))
print(chr(50))
print(ord('W'))

seq = 'ATATC'
print(seq[4],seq[0])

for nt in seq:
	print(nt, end='') #end for the blank print to work
print()

for i in range(len(seq)):
	print(i, seq[i])
	
s = 'ABCDEFGHIJ'
print(s[0:5])
print(s[0:8:2]) #goes by 2's

tax = ('Homo', 'sapiens', 9606)
print(tax) 
print(tax[0]) 
print(tax[::-1])   # slice : reverses the order?

nts = 'ACGT'
for i in range(len(nts)):
    print(i, nts[i])
    
for i, nt in enumerate(nts): #usage is similar to the range(len) for tuples
    print(i, nt)
    
'''
def min(n):
	min_current = n[0]
	for i in range(len(n)):
		if i < n[1:]:
			min_current = i
		return min_current

def minimum(vals):
	mini = vals[0]
	for val in vals[1:]:
		if val < mini:
			mini = val
	return mini
'''
#print(minimum([3,4,5,6,2,10]))

def minmax(vals):
	mini = vals[0]
	maxi = vals[0]
	for val in vals[1:]: #note review usage of [1:]
		if val < mini:
			mini = val
		if val > maxi:
			maxi = val
	return mini, maxi
print(minmax([3,4,5,6,2,10]))

def mean(vals):
	total = 0
	for val in vals:
		total += val
	return total/ len(vals)
print(mean([5,10,20]))

import math
def entropy(vals):
	H = 0
	for val in vals:
		H += -val * math.log2(val)
	return H
print(entropy([0.2, 0.3, 0.5]))

def dk1(P, Q):
	d = 0
	for p,q in zip (P, Q):
		d += p * math.log2(p/q)
	return d
p1 = [0.4, 0.3, 0.2, 0.1]
p2 = [0.1, 0.3, 0.4, 0.2]
print(dk1(p1, p2))
'''
import sys
print(sys.argv)





