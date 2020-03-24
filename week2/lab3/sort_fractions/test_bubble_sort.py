import unittest
from sort_fractions import bubble_sort

class TestBubbleSort(unittest.TestCase):
	def test_returns_empty_list_if_emtpy_list_passed(self):
		#ARRANGE
		fractions = []

		#ACT
		result = bubble_sort(fractions)

		#ASSERT
		self.assertEqual(result, [])
		
	def test_returns_sorted_list_of_fractions_in_ascending_order(self):
		#ARRANGE
		fractions = [(2, 5), (5, 10), (1, 6)]

		#ACT
		result = bubble_sort(fractions)

		#ASSERT
		self.assertEqual(result, [(1, 6), (2, 5), (5, 10)])
		
	def test_returns_sorted_list_of_fractions_in_descending_order(self):
		#ARRANGE
		fractions = [(2, 5), (5 ,10), (1, 6)]
		ascending = False
		#ACT
		result = bubble_sort(fractions, ascending)

		#ASSERT
		self.assertEqual(result, [(5, 10), (2, 5), (1, 6)])




if __name__ == '__main__':
	unittest.main()