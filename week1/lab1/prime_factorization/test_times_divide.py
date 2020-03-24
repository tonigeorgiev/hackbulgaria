import unittest
from prime_factorization import times_divide
class TestTimesDivide(unittest.TestCase):
	def test_returns_how_many_times_one_number_devides_another(self):
		#ARRANGE
		n = 16
		divider = 2

		#ACT
		result = times_divide(n, divider)

		#ASSERT
		self.assertEqual(result, 4)




if __name__ == '__main__':
	unittest.main()