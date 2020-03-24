def is_prime(n):
	for x in range(2, n):
		if n % x == 0:
			return False
	return True

def find_next_prime_divider(n, divider):
	if divider < 2:
		return 2
	if is_prime(divider + 1) and n % (divider + 1) == 0:
		return divider+1
	return find_next_prime_divider(n, divider + 1)


def times_divide(n, divider):
	result = 0
	while n != 1 and n % divider == 0:
		result += 1
		n = n // divider
	return result

def prime_factorization(n):
	while n != 1:
		pass
