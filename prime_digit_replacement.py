import math

def isaiah_primechecker(num):
	if num % 2 == 0:
		return False
	else:
		for i in range(int(math.sqrt(num)/2)):
			divisor = 2*i+3
			#print(divisor)
			if num % divisor == 0:
				return False
				break
	return True

for i in range(20):
	primes = isaiah_primechecker(i)
	if primes == True:
		print(i,end=": ")
		print(primes)
