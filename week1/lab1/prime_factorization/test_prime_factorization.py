import unittest
from prime_factorization import find_next_prime_divider
class FindNextPrimeDivider(unittest.TestCase):
	def test_returns_next_prime_divider_after_current_for_n(self):
		#ARRANGE
		n = 10
		divider = 2

		#ACT
		result = find_next_prime_divider(n, divider)

		#ASSERT
		self.assertEqual(result, 5)
	def test_returns_two_if_number_bellow_two_passed_as_argument(self):
		#ARRANGE
		n = 10
		divider = -5

		#ACT
		result = find_next_prime_divider(n, divider)

		#ASSERT
		self.assertEqual(result, 2)




if __name__ == '__main__':
	unittest.main()