import unittest
from nan_expand import nan_expand_helper, nan_expand

class TestNaNExpandHelper(unittest.TestCase):
	def test_returns_empty_string_if_zero_passed_as_argument(self):
		#ARRANGE
		times = 0

		#ACT
		result = nan_expand_helper(times, '')

		#ASSERT
		self.assertEqual(result, '')
	def test_returns_one_repeat_of_the_string_if_one_passed_as_argument(self):
		#ARRANGE
		times = 1

		#ACT 
		result = nan_expand_helper(times, '')
		expected = 'Not a NaN'

		#ASSERT
		self.assertEqual(result, expected)

	def test_returns_n_repeats_of_the_string_if_n_passed_as_argument(self):
		#ARRANGE
		times = 3

		#ACT 
		result = nan_expand_helper(times, '')
		expected = 'Not a Not a Not a NaN'

		#ASSERT
		self.assertEqual(result, expected)

class TestNaNExpansion(unittest.TestCase):
	def test_raises_error_if_not_int_passed(self):
		#ARRANGE
		times = 'a'
		exc = None
		#ACT
		try: 
			nan_expand(times)
		except Exception as err:
			exc = err
		

		#ASSERT
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid input')

if __name__ == '__main__':
	unittest.main()