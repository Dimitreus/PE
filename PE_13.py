file = open('PE_13_support.txt', "r")
result = 0
for line in file:
	line = int(line)
	result += line
result = str(result)[:10]
print(result)
