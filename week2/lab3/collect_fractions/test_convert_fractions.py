import unittest
from collect_fractions import convert_fractions

class TestConvertFractions(unittest.TestCase):
	def test_returns_converted_fractions_under_common_denominator(self):
		#ARRANGE
		fractions = [(1, 7), (2, 6)]
		lcm = 42
		#ACT
		result = convert_fractions(fractions, 42)
		expected = [(6, 42), (14, 42)]
		#ASSERT
		self.assertEqual(result, expected)


if __name__ == '__main__':
	unittest.main()