import math
import time
def is_prime(number):
	if number < 2:
		return False
	elif number == 2:
		return True
	for check in range(2, int(math.sqrt(number)+1)):
		if number % check == 0:			
			return False
	return True

ctime = time.time()
i = 1
result = 0
primes = [2]
while i < 2000000:
	if is_prime(i):
		result += i
	i += 2
'''

for prime in primes:
	prime = int(prime)
	result += prime
'''
print(result + 2)
print("Time: " + str(time.time() - ctime))