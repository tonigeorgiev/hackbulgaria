import unittest
from to_number import to_number


class TestToNumber(unittest.TestCase):
	def test_returns_number_of_the_digits_of_the_passed_list(self):
		#ARRANGE
		digits = [3,7,4,9]

		#ACT
		result = to_number(digits)

		#ASSERT
		self.assertEqual(result, 3749)


if __name__ == '__main__':
	unittest.main()