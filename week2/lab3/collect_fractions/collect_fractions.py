def validate(fractions):
	if not isinstance(fractions, list):
		raise TypeError('Invalid input')

	for i in fractions:
		if not isinstance(i, tuple) or len(i) != 2:
			raise TypeError('Invalid input')
		if i[1] == 0:
			raise TypeError('Zero devision')


def find_gcd(first_num, second_num):
	first_num = abs(first_num)
	second_num = abs(second_num)

	while second_num != 0:
		(first_num, second_num) = (second_num, first_num % second_num)
	return first_num

def find_lcm(first_num, second_num):
	return (first_num * second_num) / find_gcd(first_num, second_num)
	
def find_lcm_list(denominators):
	lcm = find_lcm(denominators[0], denominators[1])
	for i in range(2, len(denominators)):
		lcm = find_lcm(lcm, denominators[i])
	return lcm

def convert_fractions(fractions, lcm):
	result = []
	for fraction in fractions:
		new_nominator = fraction[0] * (lcm / fraction[1])
		new_denominator = lcm
		result.append((new_nominator, new_denominator))
	return result


def collect_fractions(fractions):
	validate(fractions)
	
	if fractions == []:
		return 0;

	if len(fractions) == 1:
		return fractions[0]

	denominators = [x[1] for x in fractions]
	lcm = find_lcm_list(denominators)

	fractions = convert_fractions(fractions, lcm)
	
	nominator_collection = sum([x[0] for x in fractions])
	return (nominator_collection, lcm)