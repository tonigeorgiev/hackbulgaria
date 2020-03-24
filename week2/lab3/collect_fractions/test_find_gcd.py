import unittest
from simplify_fractions import find_gcd

class TestFindNod(unittest.TestCase):
	def test_returns_nod_of_two_numbers(self):
		#ARRANGE
		first_number = 462
		second_number = 63
		
		#ACT
		result = find_gcd(first_number, second_number)

		#ASSERT
		self.assertEqual(result, 21)

	def test_returns_positive_gcd_for_negative_numbers(self):
		#ARRANGE
		first_number = -462
		second_number = -63
		
		#ACT
		result = find_gcd(first_number, second_number)

		#ASSERT
		self.assertEqual(result, 21)

	def test_returns_other_number_if_zero_passed_as_argument(self):
		#ARRANGE
		first_number = 0
		second_number = 5
		
		#ACT
		result = find_gcd(first_number, second_number)

		#ASSERT
		self.assertEqual(result, 5)	

if __name__ == '__main__':
	unittest.main()