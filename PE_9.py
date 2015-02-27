import math
summ = 1000		
for a in range(1, 350):
	for b in range(1, 500):
		c = 1000 - a - b
		if (a*a +b*b == c*c):
			print(a, b, c)
			break
		b += 1
	a+=1
