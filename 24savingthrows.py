import math
import random

trials = 100000
dc = 5

def advantage():
	roll1 = random.randint(1,20)
	roll2 = random.randint(1,20)
	if roll1 > roll2:
		return roll1
	else:
		return roll2
		
def disadvantage():
	roll1 = random.randint(1,20)
	roll2 = random.randint(1,20)
	if roll1 < roll2:
		return roll1
	else:
		return roll2
	
for dc in range(5,16,5):
	sucess = 0
	for i in range(trials):
		roll = random.randint(1,20)
		if roll >= dc: 
			sucess +=1
	print('Nor:', dc, sucess/trials)

for dc in range(5,16,5):	
	for i in range(trials):
		roll = advantage()
		if roll >= dc: 
			sucess +=1
	print('Adv:', dc, sucess/trials)

for dc in range(5,16,5):	
	for i in range(trials):
		roll = disadvantage()
		if roll >= dc: 
			sucess +=1
	print('Dis:', dc, sucess/trials)