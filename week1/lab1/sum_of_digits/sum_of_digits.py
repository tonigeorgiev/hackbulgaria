def sum_of_digits(n):
	if type(n) != int:
		raise TypeError('Invalid input')

	return sum([int(x) for x in str(abs(n))])
