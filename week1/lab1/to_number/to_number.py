def validate(digits):
	if digits == []:
		raise TypeError('Invalid input')

	for dig in digits:
		if type(dig) != int:
			raise TypeError('Invalid input')

def to_number(digits):
	validate(digits)

	result = ''
	for dig in digits:
		result += str(dig)

	return int(result) #or int(''.join([str(x) for x in digits]))