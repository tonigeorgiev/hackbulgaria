import numbers
def validate(iterable, key = ''):
	if not isinstance(iterable, list) and not isinstance(iterable, tuple):
		raise TypeError('Invalid input')
	if key == '':
		for i in iterable:
			if not isinstance(i, numbers.Number):
				raise TypeError('Invalid input')
	else:	
		for i in iterable:
			if not isinstance(i, dict) or not key in i:
				raise TypeError('Invalid input')


def compare(ascending, first_obj, second_obj, key = ''):
	if key == '':
		if ascending:
			return first_obj > second_obj
		return second_obj > first_obj

	if ascending:
		return first_obj[key] > second_obj[key]
	return second_obj[key] > first_obj[key]


def bubble_sort(iterable, ascending = True, key = ''):
	for i in range(0, len(iterable) - 1):
		for j in range(0, len(iterable) - 1):
			if compare(ascending, iterable[j], iterable[j+1], key):
				iterable[j], iterable[j+1] = iterable[j + 1], iterable[j]
	return iterable


def my_sort(iterable = None, ascending = True, key = ''):
	validate(iterable, key)
	if type(iterable) is tuple:
		return tuple(bubble_sort(list(iterable), ascending))
	return bubble_sort(iterable, ascending, key)

