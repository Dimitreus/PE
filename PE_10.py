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

i = 1
primes = [2]
while i < 2000000:
	if is_prime(i):
		primes.append(i)
	i += 2

result = 0
for prime in primes:
	prime = int(prime)
	result += prime

print(result)
