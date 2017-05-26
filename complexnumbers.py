import math
from copy import deepcopy

class Real:

	type = "real";
	
	def __init__(self, value):
		self.value = value;
	
	def Add(self, value):
		self.value += value;
	
	def Subtract(self, value):
		self.value -= value;
	
	def Multiply(self, value):
		self.value *= value;
	
	def Divide(self, value):
		self.value /= value;
		
	def DisplayValue(self):
		print "Value = " + str(self.value) + ".";
		
	def PrintType(self):
		print "The original type is: " + self.type;
		
		
class Complex:

	type = "complex";
	def __init__ (self, real, imaginary):
		self.real = real;
		self.imaginary = imaginary;
		
	def Add(self, complexValue):
		self.real += complexValue.real;
		self.imaginary += complexValue.imaginary
	
	def Subtract(self, complexValue):
		self.real -= complexValue.real;
		self.imaginary -= complexValue.imaginary;
		
	def Multiply(self, complexValue):
		phasor1 = self.ConvertToPhasor();
		phasor2 = complexValue.ConvertToPhasor();
		newMagnitude = phasor1['mag'] * phasor2['mag'];
		newAngle = phasor1['angle'] + phasor2['angle'];
		
		result = self.ConvertToRectangular({
			'mag': newMagnitude,
			'angle': newAngle,
		});
		
		self.real = result['real'];
		self.imaginary = result['imaginary'];
		
	def Divide(self, complexValue):
		phasor1 = self.ConvertToPhasor();
		phasor2 = complexValue.ConvertToPhasor();
		
		newMagnitude = phasor1['mag'] / phasor2['mag'];
		newAngle = phasor1['angle'] - phasor2['angle'];
		
		result = self.ConvertToRectangular({
			'mag': newMagnitude,
			'angle': newAngle,
		});
		
		self.real = result['real'];
		self.imaginary = result['imaginary'];
	
	def ConvertToPhasor(self):
		mag = (self.real**2 + self.imaginary**2)**.5;
		angle = math.atan2(self.imaginary, self.real);
		return {
			'mag': mag,
			'angle': angle,
		};
		
	def ConvertToRectangular(self, phasor):
		real = phasor['mag'] * math.cos(phasor['angle']);
		imaginary = phasor['mag'] * math.sin(phasor['angle']);
		return {
			'real': real,
			'imaginary': imaginary,
		};
		
	def DisplayValue(self):
		print "Value = " + str(self.real) + " + j" + str(self.imaginary) + ".";
		
	def PrintType(self):
		print "The type is: " + self.type;
		super;

	def __CheckOtherIsValid(self, other):
		if not isinstance(other, Complex):
			raise Exception('Other value must be a complex number')

	def __add__(self, other):
		self.__CheckOtherIsValid(other)
		result = deepcopy(self)
		result.Add(other)
		return result

	def __sub__(self, other):
		self.__CheckOtherIsValid(other)
		result = deepcopy(self)
		result.Subtract(other)
		return result

	def __mul__(self, other):
		self.__CheckOtherIsValid(other)
		result = deepcopy(self)
		result.Multiply(other)
		return result

	def __div__(self, other):
		self.__CheckOtherIsValid(other)
		result = deepcopy(self)
		result.Divide(other)
		return result