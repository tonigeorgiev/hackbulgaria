import unittest
from terms import Term

class TestTerms(unittest.TestCase):
	def test_returns_object_terms_with_two_fields_if_string_with_x_on_power_passed(self):
		#ARRANGE
		term_string = '2x^3'

		#ACT
		first = Term(term_string)

		#ASSERT
		self.assertEqual(first.constant, 2)
		self.assertEqual(first.power, 3)

	def test_returns_object_terms_with_one_field_if_string_with_x_on_no_power_passed(self):
		#ARRANGE
		term_string = '2x'

		#ACT
		first = Term(term_string)

		#ASSERT
		self.assertEqual(first.constant, 2)

	def test_returns_object_terms_with_one_field_if_string_with_only_constant_passed(self):
		#ARRANGE
		term_string = '2'

		#ACT
		first = Term(term_string)

		#ASSERT
		self.assertEqual(first.constant, 2)

if __name__ == '__main__':
	unittest.main()