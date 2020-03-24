import unittest
from sum_of_digits import sum_of_digits
class TestSumOfDigits(unittest.TestCase):
	def test_raise_exception_if_not_number(self):
		#ARRANGE
		n = 'x'
		exc = None 

		#ACT
		try:
			sum_of_digits(n)
		except Exception as err:
			exc = err
			
		#ASSERT
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid input')

	def test_returns_zero_for_input_zero(self):
		#ARRANGE
		n = 0

		#ACT
		result = sum_of_digits(n)

		#ASSERT
		self.assertEqual(result, 0)

	def test_returns_num_for_random_number(self):
		#ARRANGE
		n = 22883292

		#ACT
		result = sum_of_digits(n)

		#ASSERT
		self.assertEqual(result, 36)

	def test_returns_num_for_random_negative_number(self):
		#ARRANGE
		n = -1285

		#ACT
		result = sum_of_digits(n)

		#ASSERT
		self.assertEqual(result, 16)


if __name__ == '__main__':
	unittest.main()