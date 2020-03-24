import unittest
from collect_fractions import collect_fractions

class TestCollectFractions(unittest.TestCase):
	def test_returns_collection_of_tuples_as_fractions(self):
		#ARRANGE
		fractions = [(1, 7), (2, 6)]

		#ACT
		result = collect_fractions(fractions)

		#ASSERT
		self.assertEqual(result, (20, 42))

	def test_returns_zero_if_empty_list_passed(self):
		#ARRANGE
		fractions = []

		#ACT
		result = collect_fractions(fractions)

		#ASSERT
		self.assertEqual(result, 0)

	def test_returns_the_exact_tuple_passed_if_list_consists_of_one_tuple(self):
		#ARRANGE
		fractions = [(1, 7)]

		#ACT
		result = collect_fractions(fractions)

		#ASSERT
		self.assertEqual(result, (1, 7))


if __name__ == '__main__':
	unittest.main()