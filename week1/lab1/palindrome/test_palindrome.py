import unittest
from palindrome import palindrome

class Palindrome(unittest.TestCase):
	def test_returns_true_if_num_is_palindrome(self):
		#ARRANGE
		number = 121

		#ACT
		result = palindrome(number)

		#ASSERT
		self.assertTrue(result)

	def test_returns_true_if_word_is_palindrome(self):
		#ARRANGE
		word = 'abba'

		#ACT
		result = palindrome(word)

		#ASSERT
		self.assertTrue(result)

	def test_returns_true_if_passed_digit(self):
		#ARRANGE
		word = 1

		#ACT
		result = palindrome(word)

		#ASSERT
		self.assertTrue(result)

	def test_returns_true_if_passed_symbol(self):
		#ARRANGE
		word = 'a'

		#ACT
		result = palindrome(word)

		#ASSERT
		self.assertTrue(result)

	def test_returns_true_if_passed_nothing(self):
		#ARRANGE
		word = ''

		#ACT
		result = palindrome(word)

		#ASSERT
		self.assertTrue(result)


if __name__ == '__main__':
	unittest.main()