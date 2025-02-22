'''
20 is revivie
3 sucesses 10+ is stable 
3 failures is death 1-9
or 2 1's

cant roll dice more than 5

need to keep track of if we revived or not
how many times we died, is stable or recovers

'''
import random

trials = 10000
die = 0
stable = 0
revive = 0

for i in range(trials):
	failure = 0
	sucess = 0
	for i in range(5):
		r = random.randint(1,20)
		if r == 1: 
			failure +=2
		elif r <= 9: 
			failure +=1
		elif r <= 19: 
			sucess +=1
		else: 
			revive +=1
			break
		if sucess == 3:
			stable +=1
			break
		elif failure == 3:
			die +=1
			break
print('Death: ', die/trials)
print('Stable:', stable/trials)
print('Revive:', revive/trials)
			
			