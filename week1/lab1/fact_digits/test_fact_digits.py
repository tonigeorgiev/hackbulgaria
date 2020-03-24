import unittest
from fact_digits import fact_digits

class FactDigits(unittest.TestCase):
	def test_returns_sum_of_fact_of_each_digit_of_the_input(self):
		#ARRANGE
		digits = 145

		#ACT
		result = fact_digits(digits)
		
		#ASSERT
		self.assertEqual(result, 145)

	def test_returns_one_for_number_zero(self):
		#ARRANGE
		digits = 0

		#ACT
		result = fact_digits(digits)
		
		#ASSERT
		self.assertEqual(result, 1)

	def test_returns_positive_sum_for_negative_num(self):
		#ARRANGE
		digits = -145

		#ACT
		result = fact_digits(digits)

		#ASSERT
		self.assertEqual(result, 145)




if __name__ == '__main__':
	unittest.main()