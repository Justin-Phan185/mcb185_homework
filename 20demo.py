import math

tuple = 1,5,4,'person'
print(tuple)
print(tuple[3])

def midpoint(x1, y1, x2, y2):
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    return x, y
print(midpoint(5,5,4,4))
'''
i = 0
for i in range(i,101,3):
	print('nice',i, sep='')
'''

def triangular(tri):
	num = 0
	for i in range(tri+1): #missed the +1 so was getting the previous trinagular number
		num = num + i
	return num
print(triangular(5))


def factorial(n):
	if n == 0:
		return 1
	fac = 1
	working_fac = n
	for i in range(n):
		fac = fac * (working_fac)
		working_fac -= 1		
	return fac
#print(factorial(0))

def poisson(n, k):
	poi = n**k * math.e**-n / factorial(k)
	return poi
print(poisson(2,2))

def n_choose_k (n,k):
	result = factorial(n) / (factorial(k) * factorial(n-k))
	return result
print(n_choose_k(2,2))

def euler(trials):
	e = 0
	for i in range(trials):
		e = e + (1 / factorial(i))
	return e
print(euler(100))


def is_prime(n):
	for i in range(2, n//2 +1):
		if n % i == 0:
			return False
	return True
print(is_prime(8))


def nil(n):
	pi = 3
	for i in range(1,n):
		n = 2 * i
		divide = n * (n+1) * (n+2)
		if i % 2 == 0:
			pi -= 4/divide
		else: 
			pi += 4/divide
	return pi
print(nil(100))