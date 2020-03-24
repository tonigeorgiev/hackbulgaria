import unittest
from to_number import validate


class TestValidate(unittest.TestCase):
	def test_raises_exception_if_the_list_has_not_int_value(self):
		#ARRANGE
		digits = [1, 2, 4, '2']
		exc = None

		#ACT
		try:
			validate(digits)
		except Exception as err:
			exc = err

		#ASSERT
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid input')

	def test_raises_exception_if_emty_list_is_passed(self):
		#ARRANGE
		digits = []
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