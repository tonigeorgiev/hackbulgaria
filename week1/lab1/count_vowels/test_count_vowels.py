import unittest
from count_vowels import count_vowels, is_vowel

class CountVowels(unittest.TestCase):
	def test_returns_number_of_vowoles_in_text(self):
		#ARRANGE
		text = 'boat'

		#ACT
		result = count_vowels(text)

		#ASSERT
		self.assertEqual(result, 2)

	def test_returns_zero_if_empty_text_passed(self):
		#ARRANGE
		text = ''

		#ACT
		result = count_vowels(text)

		#ASSERT
		self.assertEqual(result, 0)





class IsVowel(unittest.TestCase):
	def test_returns_true_if_passed_symbol_is_vowel(self):
		#ARRANGE
		letter = 'a'

		#ACT
		result = is_vowel(letter)

		#ASSERT
		self.assertTrue(result)

	def test_returns_false_if_passed_symbol_is_number(self):
		#ARRANGE
		letter = 5

		#ACT
		result = is_vowel(letter)

		#ASSERT
		self.assertFalse(result)



if __name__ == '__main__':
	unittest.main()