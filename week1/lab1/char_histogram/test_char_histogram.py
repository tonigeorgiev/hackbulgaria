import unittest
from char_histogram import char_histogram

class TestCharHistogram(unittest.TestCase):
	def test_result_of_function_with_expected_result(self):
		#ARRANGE
		text = "PytthonP"
		expected = {'P':2, 'y': 1, 't':2, 'h':1, 'o':1, 'n':1}

		#ACT
		result = char_histogram(text)

		#ASSERT
		self.assertEqual(result, expected)
	def test_histogram_with_an_empty_string(self):
		#ARRANGE
		text = ""
		expected = {}

		#ACT
		result = char_histogram(text)

		#ASSERT
		self.assertEqual(result, expected)
	def test_histogram_with_object_that_is_not_string(self):
		#ARRANGE
		text = 32
		expected = {'3':1, '2':1}

		#ACT
		result = char_histogram(text)

		#ASSERT
		self.assertEqual(result, expected)

if __name__ == '__main__':
	unittest.main()