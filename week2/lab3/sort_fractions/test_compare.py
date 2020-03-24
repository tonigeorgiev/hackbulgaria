import unittest
from sort_fractions import compare

class TestPythonSort(unittest.TestCase):
	def test_returns_true_if_ascending_arguemnts_is_true_and_first_fraction_is_greater_than_the_second_fraction(self):
		#ARRANGE
		first_fraction = (3, 10)
		second_fraction = (1, 5)

		#ACT
		result = compare(first_fraction, second_fraction)

		#ASSERT
		self.assertTrue(result)

	def test_returns_true_if_ascending_arguemnts_is_false_and_second_fraction_is_greater_than_the_first_fraction(self):
		#ARRANGE
		first_fraction = (1, 4)
		second_fraction = (1, 3)

		#ACT
		result = compare(first_fraction, second_fraction, False)

		#ASSERT
		self.assertTrue(result)

	




if __name__ == '__main__':
	unittest.main()