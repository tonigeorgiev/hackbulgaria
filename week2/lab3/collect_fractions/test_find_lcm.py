import unittest
from collect_fractions import find_lcm

class TestFindLCM(unittest.TestCase):
	def test_returns_lcm_of_two_numbers(self):
		#ARRANGE
		first_number = 7
		second_number = 3

		#ACT
		result = find_lcm(first_number, second_number)

		#ASSERT
		self.assertEqual(result, 21)


if __name__ == '__main__':
	unittest.main()