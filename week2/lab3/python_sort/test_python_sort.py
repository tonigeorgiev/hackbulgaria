import unittest
from python_sort import my_sort

class TestPythonSort(unittest.TestCase):
	def test_returns_empty_list_if_passed_empty_list(self):
		#ARRANGE
		iterable = []

		#ACT
		result = my_sort(iterable)

		#ASSERT
		self.assertEqual(result, [])

	def test_returns_sorted_list_in_ascending_order(self):
		#ARRANGE
		iterable = [6, 1, 7, 4, 2]
		
		#ACT
		result = my_sort(iterable)

		#ASSERT
		self.assertEqual(result, [1, 2, 4, 6, 7])

	def test_returns_sorted_tuple_in_descending_order(self):
		#ARRANGE
		iterable = [6, 1, 7, 4, 2]
		ascending = False

		#ACT
		result = my_sort(iterable, ascending)

		#ASSERT
		self.assertEqual(result, [7, 6, 4, 2, 1])

	def test_returns_empty_tuple_if_passed_empty_tuple(self):
		#ARRANGE
		iterable = ()

		#ACT
		result = my_sort(iterable)

		#ASSERT
		self.assertEqual(result, ())

	def test_returns_sorted_tuple_in_ascending_order(self):
		#ARRANGE
		iterable = (6, 1, 7, 4, 2)
		
		#ACT
		result = my_sort(iterable)

		#ASSERT
		self.assertEqual(result, (1, 2, 4, 6, 7))

	def test_returns_sorted_tuple_in_descending_order(self):
		#ARRANGE
		iterable = (6, 1, 7, 4, 2)
		ascending = False

		#ACT
		result = my_sort(iterable, ascending)

		#ASSERT
		self.assertEqual(result, (7, 6, 4, 2, 1))

	def test_returns_sorted_list_of_dict_in_ascending_order(self):
		#ARRANGE
		iterable=[{'name': 'Marto', 'age': 24},
				  {'name': 'Ivo', 'age': 27}, 
				  {'name': 'Sashko', 'age': 25}]
		ascending = True
		key = 'age'
		#ACT
		result = my_sort(iterable, ascending, key)
		expected = [{'name': 'Marto', 'age': 24}, 
					{'name': 'Sashko', 'age': 25}, 
					{'name': 'Ivo', 'age': 27}]

		#ASSERT
		self.assertEqual(result, expected)

	def test_returns_sorted_list_of_dict_in_descending_order(self):
		#ARRANGE
		iterable=[{'name': 'Marto', 'age': 24},
				  {'name': 'Ivo', 'age': 27}, 
				  {'name': 'Sashko', 'age': 25}]
		ascending = False
		key = 'age'
		
		#ACT
		result = my_sort(iterable, ascending, key)
		expected = [{'name': 'Ivo', 'age': 27}, 
					{'name': 'Sashko', 'age': 25}, 
					{'name': 'Marto', 'age': 24}]

		#ASSERT
		self.assertEqual(result, expected)


if __name__ == '__main__':
	unittest.main()