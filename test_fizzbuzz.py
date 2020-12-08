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
  
  