import unittest
from fizzbuzz import FizzBuzz


class TestFizzBuzz(unittest.TestCase):

	def test_ini(self):
		self.fizzbuzz = FizzBuzz()

	def test_number(self):
		self.assertEqual(FizzBuzz().fizzbuzz[3], '4')
		self.assertEqual(FizzBuzz().fizzbuzz[7], '8')
		self.assertEqual(FizzBuzz().fizzbuzz[42], '43')

	def test_fizz(self):
		self.assertEqual(FizzBuzz().fizzbuzz[2], 'fizz')
		self.assertEqual(FizzBuzz().fizzbuzz[11], 'fizz')

	def test_buzz(self):
		self.assertEqual(FizzBuzz().fizzbuzz[19], 'buzz')
		self.assertEqual(FizzBuzz().fizzbuzz[79], 'buzz')

	def test_fizzbuzz(self):
		self.assertEqual(FizzBuzz().fizzbuzz[14], 'fizzbuzz')
		self.assertEqual(FizzBuzz().fizzbuzz[74], 'fizzbuzz')

	def test_custom_range_constructor(self):
		self.assertEqual(FizzBuzz(14, 43).fizzbuzz[12], '26')
		self.assertEqual(FizzBuzz(43, 14).fizzbuzz[74], 'fizzbuzz')

	def test_at(self):
		self.assertEqual(FizzBuzz().at(200), 'buzz')
		self.assertEqual(FizzBuzz().at(420), 'fizzbuzz')
		self.assertEqual(FizzBuzz().at('p'), None)
