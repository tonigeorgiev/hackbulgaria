from utils import parse_string_to_term_information
class Term():
	def __init__(self, term_string):
		information = parse_string_to_term_information(term_string)
		self.constant = int(information[0])
		if information[1] != '':
			self.power = int(information[1])