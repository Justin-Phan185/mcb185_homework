import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

collisions = 0
for i in range(trials):
	birthdays = []
	for i in range(people):
		birthday = random.randint(0,days-1)
		birthdays.append(birthday)
	collision = False
	for i in range(people):
		date_match = birthdays[i]
		for day in birthdays[i+1:]:
			if day == date_match:
				collision = True
	if collision is True:
		collisions +=1
		
print(collisions / trials)