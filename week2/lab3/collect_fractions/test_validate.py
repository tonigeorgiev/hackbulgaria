import unittest
from collect_fractions import validate

class TestValidate(unittest.TestCase):
	def test_raises_exception_if_not_all_elements_are_tuple(self):
		#ARRANGE
		fractions = [(1, 3), (1, 8), 4]
		exc = None

		#ACT
		try:
			validate(fractions)
		except Exception as err:
			exc = err

		#ASSERT
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid input')

	def test_raises_exception_if_tuple_has_more_than_two_arguments(self):
		#ARRANGE
		fractions = [(1, 3, 5), (1, 8), (4, 1, 4)]
		exc = None

		#ACT
		try:
			validate(fractions)
		except Exception as err:
			exc = err

		#ASSERT
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid input')

	def test_raises_exception_if_tuple_has_zero_as_denominator(self):
		#ARRANGE
		fractions = [(1, 3), (1, 8), (4, 0)]
		exc = None

		#ACT
		try:
			validate(fractions)
		except Exception as err:
			exc = err

		#ASSERT
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Zero devision')

	def test_raises_exception_fractions_not_list(self):
		#ARRANGE
		fractions = (1, 3)
		exc = None

		#ACT
		try:
			validate(fractions)
		except Exception as err:
			exc = err

		#ASSERT
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid input')

if __name__ == '__main__':
	unittest.main()