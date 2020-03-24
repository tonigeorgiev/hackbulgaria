def nan_expand_helper(times, string):
	if times == 0:
		return ''
	if times == 1:
		return string + 'Not a NaN'
	return nan_expand_helper(times - 1, string + 'Not a ')

def nan_expand(times):
	if type(times) != int:
		raise TypeError('Invalid input')
	return nan_expand_helper(times, '')
