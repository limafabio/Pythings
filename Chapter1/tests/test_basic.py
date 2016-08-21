#!/usr/bin/py

# name file: Fraction.py
#
# Author: Fabio Lima
# Version 1 08/07/2016
# GPL License
# ---------------------
# It's a Fraction class with a binary operators with test in the main
# Develop with python 2.7

import unittest
from .context import Fraction

class TestMethods(unittest.TestCase):

    def test_init(self):
        test = Fraction(1,2)
        self.assertEqual(Fraction(1,2),test)

    def test_gdc(self):
        test = Fraction(1,2)
        self.assertEqual(test.gdc(2,4),2)

    def test_floor(self):
        test = Fraction(2,3)
        self.assertEqual(test.floor(),0)

    def test_ceil(self):
        test = Fraction(7,10)
        self.assertEqual(test.ceil(),1)

    def test_abs(self):
        test = Fraction(-1,2)
        other = Fraction(1,2)
        self.assertEqual(abs(test),other)

    def teste_add(self):
        test = Fraction(1,2)
        other = Fraction(1,3)
        result = Fraction(5,6)
        self.assertEqual(test + other, result)

    def teste_eq(self):
        test = Fraction(1,2)
        other = Fraction(1,2)
        self.assertEqual(test == other,True)

    def teste_ge(self):
        test = Fraction(1,2)
        other = Fraction(1,3)
        self.assertEqual(test >= other,True)

    def teste_gt(self):
        test = Fraction(1,2)
        other = Fraction(1,3)
        self.assertEqual(test > other,True)

    def teste_index(self):
        test = Fraction(1,2)
        other = Fraction(1,3)
        result = Fraction(1,2)
        self.assertEqual(test & other,result)

    def teste_invert(self):
        test = Fraction(1,2)
        print test.invert()

    def teste_le(self):
        test = Fraction(1,2)
        other = Fraction(1,3)
        self.assertEqual(test <= other,False)

    def teste_lt(self):
        test = Fraction(1,2)
        other = Fraction(1,3)
        self.assertEqual(other < test,True)

    def teste_mul(self):
        test = Fraction(1,2)
        other = Fraction(1,3)
        result = Fraction(1,6)
        self.assertEqual(test * other,result)

    '''
    def teste_ne(self):
        test = Fraction(1,2)
        other = Fraction(1,3)
        self.assertEqual(test != other,True)
    '''
    def teste_neg(self):
        test = Fraction(1,2)
        result = Fraction(-1,2)
        self.assertEqual(-test,result)


if __name__ == "__main__":

    unittest.main()
