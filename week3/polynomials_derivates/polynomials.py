from utils import parse_string_to_list_of_terms
from terms import Term
class Polynomial():
	def __init__(self, arguments_as_string):
		arguments_as_string_as_parts = parse_string_to_list_of_terms(arguments_as_string)
		self.terms = [Term(x) for x in arguments_as_string_as_parts]