def char_histogram(string):
	string = str(string)
	result = {}
	for x in string:
		result[x] = string.count(x)
	return result