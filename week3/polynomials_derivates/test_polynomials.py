import unittest
from polynomials import Polynomial
from terms import Term
class TestPolynomial(unittest.TestCase):
	def test_returns_object_polynom_which_has_list_of_objects_tersm(self):
		#ARRANGE
		arguments_as_string = '2x^3 + 3x + 1'

		#ACT
		first_polynom = Polynomial(arguments_as_string)

		#ASSERT
		self.assertTrue(all([isinstance(x, Term) for x in first_polynom.terms]))

if __name__ == '__main__':
	unittest.main()