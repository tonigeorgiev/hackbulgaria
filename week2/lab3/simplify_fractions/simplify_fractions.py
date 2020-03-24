def validate(fraction):
	if not isinstance(fraction, tuple) or len(fraction) != 2:
		raise TypeError('Invalid input')
	if fraction[1] == 0:
		raise TypeError('Zero devision')

def find_gcd(first_num, second_num):
	first_num = abs(first_num)
	second_num = abs(second_num)

	while second_num != 0:
		(first_num, second_num) = (second_num, first_num % second_num)
	return first_num

def simplify_fractions(num):
	validate(num)
	gcd = find_gcd(num[0], num[1])
	return (num[0]/gcd, num[1]/gcd)
