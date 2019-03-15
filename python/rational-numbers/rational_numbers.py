from __future__ import division
from fractions import gcd


class Rational(object):
    '''
        def test_reduce_positive(self):
            self.assertEqual(Rational(2, 4), Rational(1, 2))
    '''
    def __init__(self, numer, denom):
        my_gcd = gcd(numer, denom)
        self.numer = numer / my_gcd
        self.denom = denom / my_gcd

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        a1, b1, a2, b2 = self.numer, self.denom, other.numer, other.denom
        return Rational(a1 * b2 + a2 * b1, b1 * b2)

    '''
    # Test subtraction
    def test_subtract_two_positive(self):
        self.assertEqual(Rational(1, 2) - Rational(2, 3), Rational(-1, 6))

The difference of two rational numbers r1 = a1/b1 and r2 = a2/b2 is r1 - r2 = a1/b1 - a2/b2 = (a1 * b2 - a2 * b1) / (b1 * b2).
    '''

    def __sub__(self, other):
        a1, b1, a2, b2 = self.numer, self.denom, other.numer, other.denom
        return Rational(a1 * b2 - a2 * b1, b1 * b2)

    def __mul__(self, other):
        a1, b1, a2, b2 = self.numer, self.denom, other.numer, other.denom
        return Rational(a1 * a2, b1 * b2)

    def __truediv__(self, other):
        a1, b1, a2, b2 = self.numer, self.denom, other.numer, other.denom
        return Rational(a1 * b2, a2 * b1)
        
    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))


    def __pow__(self, power):
        return Rational(self.numer ** power, self.denom ** power)

    def __rpow__(self, base):
        return base ** (self.numer / self.denom)
