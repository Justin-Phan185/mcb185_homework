#Pythagorean triples

import math

limit = 100

for a in range(1,limit):
	for b in range (a+1,limit): #a+1 instead of 1 to check all greater then a to remove dupes
		c = math.sqrt((a**2 + b**2))
		remainder = c%1
		if remainder == 0: print(a,b,c)