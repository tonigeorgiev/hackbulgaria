import unittest
from collect_fractions import find_lcm_list

class TestFindLCMList(unittest.TestCase):
	def test_returns_lcm_of_list(self):
		#ARRANGE
		fractions = [2, 4, 6]

		#ACT
		result = find_lcm_list(fractions)

		#ASSERT
		self.assertEqual(result, 12)


if __name__ == '__main__':
	unittest.main()