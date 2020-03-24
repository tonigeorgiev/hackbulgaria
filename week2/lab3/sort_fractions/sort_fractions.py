def validate(fractions):
	if not isinstance(fractions, list):
		raise TypeError('Invalid input')

	for i in fractions:
		if not isinstance(i, tuple) or len(i) != 2:
			raise TypeError('Invalid input')
		if i[1] == 0:
			raise TypeError('Zero devision')
	

def compare(first_fraction, second_fraction, ascending = True):
	if ascending:
		return first_fraction[0] / first_fraction[1] > second_fraction[0] / second_fraction[1]
	return second_fraction[0] / second_fraction[1] > first_fraction[0] / first_fraction[1]


def bubble_sort(iterable, ascending = True):
	for i in range(0, len(iterable) - 1):
		for j in range(0, len(iterable) - 1):
			if compare(iterable[j], iterable[j+1], ascending):
				iterable[j], iterable[j+1] = iterable[j + 1], iterable[j]
	return iterable

def sort_fractions(fractions, ascending = True):
	validate(fractions)
	return bubble_sort(fractions, ascending)

