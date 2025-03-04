import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

collisions = 0	
for i in range(trials):
	calander = []
	for i in range(days):
		calander.append(0)
	for i in range(people):
		bday = random.randint(0,days-1)
		calander[bday] +=1
	collision = False
	for i in range(len(calander)):
		if calander[i] > 1: 
			collision = True
	if collision is True:
		collisions +=1
		
print(collisions/trials)
