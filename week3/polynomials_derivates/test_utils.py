import unittest
from utils import parse_string_to_list_of_terms, parse_string_to_term_information
import terms

class TestStringToListOfTerms(unittest.TestCase):
	def test_returns_list_of_strings_as_parts_of_polynom(self):
		#ARRANGE
		polynom_string = '2x^3 + 3x + 1'

		#ACT
		result = parse_string_to_list_of_terms(polynom_string)
		expected = ['2x^3', '3x', '1']

		#ASSERT
		self.assertEqual(result, expected)

class TestStringToTermInformation(unittest.TestCase):
	def test_returns_tuple_of_two_strings_if_x_on_power_passed(self):
		#ARRANGE
		term_string = '2x^3'

		#ACT
		result = parse_string_to_term_information(term_string)
		
		#ASSERT
		self.assertEqual(result, ['2', '3'])

	def test_returns_tuple_of_one_string_and_one_empty_string_if_just_x_passed(self):
		#ARRANGE
		term_string = '2x'

		#ACT
		result = parse_string_to_term_information(term_string)
		
		#ASSERT
		self.assertEqual(result, ['2', ''])

	def test_returns_tuple_of_one_string_and_one_empty_string_if_no_x_passed(self):
		#ARRANGE
		term_string = '3'

		#ACT
		result = parse_string_to_term_information(term_string)
		
		#ASSERT
		self.assertEqual(result, ['3', ''])



if __name__ == '__main__':
	unittest.main()