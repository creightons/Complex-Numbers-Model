from complexnumbers import Real, Complex
from unittest import TestCase, main

class ComplexNumberTest(TestCase):
	def test_additionWithComplexNumber(self):
		alpha = Complex(1, 1)
		beta = Complex(2, 3)
		gamma = alpha + beta

		self.assertEqual(gamma.real, 3)
		self.assertEqual(gamma.imaginary, 4)

	def test_subtractionWithComplexNumber(self):
		alpha = Complex(1, 1)
		beta = Complex(2, 3)
		gamma = alpha - beta

		self.assertEqual(gamma.real, -1)
		self.assertEqual(gamma.imaginary, -2)

	def test_multiplicationWithComplexNumber(self):
		alpha = Complex(1, 1)
		beta = Complex(3, 5)
		gamma = alpha * beta

		self.assertEqual(gamma.real, -2)
		self.assertEqual(gamma.imaginary, 8)

	def test_divisionWithComplexNumber(self):
		alpha = Complex(8, 6)
		beta = Complex(-1, -2)
		gamma = alpha / beta

		self.assertEqual(gamma.real, -4)
		self.assertEqual(gamma.imaginary, 2.000000000000001)
		
if __name__ == '__main__':
	main()