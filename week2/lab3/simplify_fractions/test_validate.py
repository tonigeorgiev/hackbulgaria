import unittest
from simplify_fractions import validate

class TestValidate(unittest.TestCase):
	def test_raises_exception_if_tuple_does_not_have_exactly_two_elements(self):
		#ARRANGE
		fraction = (1, 3, 6)
		exc = None

		#ACT
		try:
			validate(fraction)
		except Exception as err:
			exc = err

		#ASSERT
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid input')
	
	def test_raises_exception_if_fraction_is_not_tuple(self):
		#ARRANGE
		fraction = [1, 3, 6]
		exc = None

		#ACT
		try:
			validate(fraction)
		except Exception as err:
			exc = err

		#ASSERT
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid input')

	def test_raises_exception_if_denominator_is_zero(self):
		#ARRANGE
		fraction = (4, 0)
		exc = None

		#ACT
		try:
			validate(fraction)
		except Exception as err:
			exc = err

		#ASSERT
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Zero devision')		


if __name__ == '__main__':
	unittest.main()
