import unittest
from fact_digits import validate

class Validate(unittest.TestCase):
	def test_raises_exception_if_not_int_value(self):
		#ARRANGE
		digits = 'notnumber'
		exc = None

		#ACT
		try:
			validate(digits)
		except Exception as err:
			exc = err

		#ASSERT
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid input')




if __name__ == '__main__':
	unittest.main()