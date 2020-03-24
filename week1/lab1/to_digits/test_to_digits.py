import unittest
from to_digits import to_digits

class ToDigits(unittest.TestCase):
	def test_raises_exception_if_not_number(self):
		#ARRANGE
		x = 'notnumber'
		exc = None 

		#ACT
		try:
			result = to_digits(x)
		except Exception as err:
			exc = err

		#ASSERT
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid input')

	def test_returns_list_of_the_digits_of_a_number(self):
		#ARRANGE
		x = 2923

		#ACT
		result = to_digits(x)

		#ASSERT
		self.assertEqual(result, [2,9,2,3])

	def test_returns_list_of_the_digits_of_a_negative_number(self):
		#ARRANGE
		x = 1542

		#ACT
		result = to_digits(x)

		#ASSERT
		self.assertEqual(result, [1,5,4,2])





if __name__ == '__main__':
	unittest.main()