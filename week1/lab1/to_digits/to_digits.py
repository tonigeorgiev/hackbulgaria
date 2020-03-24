def to_digits(n):
	if type(n) != int:
		raise TypeError('Invalid input')

	return [int(x) for x in str(abs(n))]