import unittest
from python_sort import validate

class TestValidate(unittest.TestCase):
	def test_raises_exc_if_passed_object_that_is_not_tuple_or_list(self):
		#ARRANGE
		iterable = {'raise exception': 1}
		exc = None

		#ACT
		try:
			validate(iterable)
		except Exception as err:
			exc = err

		#ASSERT
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid input') 

	def test_raises_exc_if_key_not_empty_string_and_iterable_has_object_that_is_not_dict(self):
		#ARRANGE
		iterable = [{'price': 1}, [1, 2, 3]]
		key = 'smth'
		exc = None

		#ACT
		try:
			validate(iterable, key)
		except Exception as err:
			exc = err

		#ASSERT
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid input') 

	def test_raises_exc_if_key_not_empty_string_and_iterable_has_dict_that_does_not_have_it_as_key(self):
		#ARRANGE
		iterable = [{'price': 1}, {'hour': 2, 'price': 1}, {'hour': 5}]
		key = 'price'
		exc = None

		#ACT
		try:
			validate(iterable, key)
		except Exception as err:
			exc = err

		#ASSERT
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid input') 

	def test_raises_exc_if_key_empty_string_and_not_all_elements_numbers(self):
		#ARRANGE
		iterable = [1, 2, 4, [1]]
		key = ''
		exc = None

		#ACT
		try:
			validate(iterable, key)
		except Exception as err:
			exc = err

		#ASSERT
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid input') 





if __name__ == '__main__':
	unittest.main()