#If we list all the natural numbers below 10 that are multiples of 3 or 5,
#we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

def summ_of_multiples(n, k):
	result = 0
	for i in range(1, n):
		if i%k == 0:
			result += i
	return result

print summ_of_multiples(1000, 3) + summ_of_multiples(1000, 5) - summ_of_multiples(1000, 15)

