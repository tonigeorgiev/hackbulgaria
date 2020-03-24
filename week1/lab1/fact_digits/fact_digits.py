import math
def validate(n):
	if type(n) != int:
		raise TypeError('Invalid input')
	return abs(n)

def fact_digits(n):
	n = validate(n)
	return sum([math.factorial(int(x)) for x in str(n)])
