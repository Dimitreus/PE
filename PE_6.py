'''
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def sum_square(k):
	result = 0
	for i in range(1, k+1):
		result += i*i
	return result

print(sum_square(100))
def square_sum(k):
	result = 0
	for i in range(1, k+1):
		result += i
	result = result*result
	return result
print(square_sum(100))

def square_sum_diff(k):
	return abs(sum_square(k) - square_sum(k))
	
print(square_sum_diff(100))
