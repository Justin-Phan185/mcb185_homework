#if num % 3 == 0 #fizz
'''
for i in range (50,-2):
	print(i)
'''	

for i in range(1,101):
	if i%3 == 0:
		print('Fizz')
	elif i%5 == 0:
		print('Buzz')
	elif i%3 and i%5 ==0:
		print('FizzBuzz')
	else:
		print(i)