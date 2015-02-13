'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''
#This thing is dirty and EXTREMLY SLOW!

import math
def is_prime(number):
	if number < 2:
		return False
	elif number == 2:
		return True
	for check in range(2, int(math.sqrt(number)+1)):
#		print(check, number, number/check)
		if number % check == 0:			
			return False
	return True
			
def factorizing(number):
	result = 0
	if is_prime(number):
		return number
	else:
		for i in range (2, int(math.sqrt(number)+1)):
			if is_prime(i) and number % i == 0:
				result = i
	return result
				
			
print (factorizing(600851475143))