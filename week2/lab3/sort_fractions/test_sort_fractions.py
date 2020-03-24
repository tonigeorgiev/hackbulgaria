import unittest
from sort_fractions import sort_fractions

class TestImportFractions(unittest.TestCase):
	def test_returns_sorted_list_of_fractions(self):
		#ARRANGE
		fractions = [(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]

		#ACT
		result = sort_fractions(fractions)
		expected = [(22, 78), (15, 32), (5, 6), (7, 8), (9, 6), (22, 7)]

		#ASSERT
		self.assertEqual(result, expected)

if __name__ == '__main__':
	unittest.main()