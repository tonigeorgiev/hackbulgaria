def validate_matrix(m):
	for rows in m:
		for symbol in rows:
			if type(symbol) != int:
				raise TypeError('Invalid input')


def sum_matrix(m):
	validate_matrix(m)
	result = 0
	for x in m:
		result += sum(x)
	return result
