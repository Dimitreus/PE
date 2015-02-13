'''
Find the largest palindrome made from the product of two 3-digit numbers.
'''

def is_palindrome(number):
	if str(number) == str(number)[::-1]:
		return True
	return False

def biggest_palindrome3():
	result = 0
	for k in range(100, 999):
		for n in range(100, 999):
			if is_palindrome(k*n) and k*n > result:
				result = k*n
	return result

print(biggest_palindrome3())