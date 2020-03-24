import unittest
from python_sort import compare

class TestPythonSort(unittest.TestCase):
	def test_returns_true_if_ascending_argument_is_true_no_value_for_key_argument_is_passed_and_first_num_greater_than_second_num(self):
		#ARRANGE
		first_num = 5
		second_num = 3
		ascending = True
		key = ''

		#ACT
		result = compare(ascending, first_num, second_num, key)

		#ASSERT
		self.assertTrue(result)

	def test_returns_true_if_ascending_argument_is_false_no_value_for_key_argument_is_passed_and_second_num_greater_than_first_num(self):
		#ARRANGE
		first_num = 3
		second_num = 6
		ascending = False
		key = ''

		#ACT
		result = compare(ascending, first_num, second_num, key)

		#ASSERT
		self.assertTrue(result)
	
	def test_returns_true_if_ascending_argument_is_true_if_value_of_first_passed_dict_is_greater_than_value_of_second_dict(self):
		#ARRANGE
		first_num = {'price':8}
		second_num = {'price':6}
		ascending = True
		key = 'price'

		#ACT
		result = compare(ascending, first_num, second_num, key)

		#ASSERT
		self.assertTrue(result)

	def test_returns_true_if_ascending_argument_is_false_value_of_second_dict_is_greater_than_value_of_first_dict(self):
		#ARRANGE
		first_dict = {'price':7}
		second_dict = {'price':9}
		ascending = False
		key = 'price'

		#ACT
		result = compare(ascending, first_dict, second_dict, key)

		#ASSERT
		self.assertTrue(result)




if __name__ == '__main__':
	unittest.main()