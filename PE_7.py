'''
What is the 10 001st prime number?
'''

import math
def is_prime(number):
	if number < 2:
		return False
	elif number == 2:
		return True
	for check in range(2, int(math.sqrt(number)+1)):
		if number % check == 0:			
			return False
	return True
	
i = 2
primes =[]
while len(primes) < 10001:
	if is_prime(i):
		primes.append(i)
	i+=1
	
print(primes[10000])
