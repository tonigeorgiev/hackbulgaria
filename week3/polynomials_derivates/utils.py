def parse_string_to_list_of_terms(polynom_string):
	polynom_parts = polynom_string.split(' + ')
	return polynom_parts

def parse_string_to_term_information(term_string):
	if 'x^' in term_string:
		return term_string.split('x^')
	elif 'x' in term_string:
		return term_string.split('x')
	return [term_string, '']
