import unittest
from count_constants import count_consonants, is_vowel, is_consonants

class CountConsonants(unittest.TestCase):
	def test_returns_number_of_consonants_in_text_with_only_letters(self):
		#ARRANGE
		text = 'boat'

		#ACT
		result = count_consonants(text)

		#ASSERT
		self.assertEqual(result, 2)

	def test_returns_number_of_consonants_in_text(self):
		#ARRANGE
		text = 'boa!tR#'

		#ACT
		result = count_consonants(text)

		#ASSERT
		self.assertEqual(result, 3)

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
		letter = '5'

		#ACT
		result = is_vowel(letter)

		#ASSERT
		self.assertFalse(result)

class IsConstant(unittest.TestCase):
	def test_returns_true_if_passed_symbol_is_a_letter_and_not_vowel(self):
		#ARRANGE
		letter = 'r'

		#ACT
		result = is_consonants(letter)

		#ASSERT
		self.assertTrue(result)

	def test_returns_false_if_passed_symbol_is_number(self):
		#ARRANGE
		letter = '5'

		#ACT
		result = is_consonants(letter)

		#ASSERT
		self.assertFalse(result)


if __name__ == '__main__':
	unittest.main()