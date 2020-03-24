import unittest
from simplify_fractions import simplify_fractions

class TestSimplifyFractions(unittest.TestCase):
	def test_returns_tuple_representing_simplified_fraction_of_other_tuple(self):
		#ARRANGE
		fraction = (3, 9)

		#ACT
		result = simplify_fractions(fraction)

		#ASSERT
		self.assertEqual(result, (1, 3))


if __name__ == '__main__':
	unittest.main()