import unittest
from python_sort import bubble_sort

class TestBubbleSort(unittest.TestCase):
	def test_returns_sorted_list_in_ascending_order(self):
		#ARRANGE
		list_one = [2, 5, 10, 1, 6]
		#ACT
		result = bubble_sort(list_one)

		#ASSERT
		self.assertEqual(result, [1, 2, 5, 6, 10])
		
	def test_returns_sorted_list_in_descending_order(self):
		#ARRANGE
		list_one = [2, 5, 10, 1, 6]
		ascending = False
		#ACT
		result = bubble_sort(list_one, ascending)

		#ASSERT
		self.assertEqual(result, [10, 6, 5, 2, 1])




if __name__ == '__main__':
	unittest.main()