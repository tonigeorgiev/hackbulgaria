import unittest
from sum_matrix import sum_matrix, validate_matrix

class TestSumMatrix(unittest.TestCase):
	def test_sum_of_two_level_nested_matrix(self):
		#ARRANGE
		matrix =  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
		expected = 45

		#ACT
		result = sum_matrix(matrix)

		#ASSERT 
		self.assertEqual(result, expected)

	def test_sum_of_empty_matrix(self):
		#ARRANGE
		matrix =  []
		expected = 0

		#ACT
		result = sum_matrix(matrix)

		#ASSERT 
		self.assertEqual(result, expected)

class ValidateMatrix(unittest.TestCase):
	def test_if_elements_of_matrix_are_not_integers(self):
		#ARRANGE
		matrix = [['a', 'b'], ['c', 'd']]
		exc = None 

		#ACT
		try:
			validate_matrix(matrix)
		except Exception as err:
			exc = err

		#ASSERT
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid input')




if __name__ == '__main__':
	unittest.main()