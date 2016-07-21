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

class Fraction:

    #initialization
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom

    #return the number to string
    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    #return the grant divisor common between m and n
    def gdc(self,m,n):
        while m%n != 0:
            old_m = m
            old_n = n

            m = old_n
            n = old_m % old_n
        return n

    #return a number convert to integer and remove decimal value
    def floor(self):
        return int(self.num / self.den)

    #return a number convert to integer around to the bigger nearest integer value
    def ceil(self):
        return int(float(self.num) / float(self.den) + 0.5)

    #return the absolute value
    def __abs__(self):
        if (self.den < 0):
            new_den = -self.den
        else:
            new_den = self.den

        if (self.num < 0):
            new_num = -self.num
        else:
            new_num = self.num
        return Fraction(new_num,new_den)

    #return fraction with sum of 2 numbers
    def __add__(self,other_fraction):
        new_num = self.num*other_fraction.den + self.den*other_fraction.num
        new_den = self.den*other_fraction.den
        common = self.gdc(new_num,new_den)
        return Fraction(new_num // common ,new_den // common)

    #return fraction with operation and 2 numbers
    def __and__(self,other):
        new_num = self.num & other.num
        new_den = self.den & other.den
        return Fraction(new_num,new_den)

    #return true if numbers are equals
    def __eq__(self,other):
        first_num = self.num *other.den
        second_num = other.num * self.den
        return first_num == second_num

    #return true if the object is bigger or equal than the other
    def __ge__(self,other):
        return self.dec() >= other.dec()

    #return true if the object is bigger than the other
    def __gt__(self,other):
        return self.dec() > other.dec()

    #return number convert in integer
    def __index__(self):
        integer = self.num / self.den
        rest = (self.num / self.den) // 1
        if (rest < 0.6):
            return  (integer - rest)
        else:
            return (integer - rest + 1)

    #return invert fraction
    def __invert__(self):
        return Fraction(~self.num,~self.den)

    #return true if the object is small or equal than the other
    def __le__(self,other):
        return self.dec() <= other.dec()

    #return true if the object is smaller than the other
    def __lt__(self,other):
        return self.dec() < other.dec()

    #return fraction with multiplication with 2 numbers
    def __mul__(self,other):
        new_den = self.num * other.num
        new_num = self.den * other.den
        return Fraction(new_den,new_num)

    #return true if the numbers are not equals
    def __ne__(self,other):
        return self != other

    #return fraction with negative number
    def __neg__(self,other):
        return Fraction(-self.num,self.den)

    #return fraction with operation not
    def __not__(self):
        new_num = not self.num
        new_den = not self.den
        return Fraction(new_num,new_den)

    #return fraction with operation or in 2 numbers
    def __or__(self,other):
        new_num = self.num | other.num
        new_den = self.den | self.den
        return Fraction(new_num, new_den)

    #return fraction with the positive number
    def __pos__(self):
        if (self.den < 0 and self.num > 0):
            new_num = self.num
            new_den = -self.den
        elif (self.den > 0 and self.num < 0):
            new_num = -self.num
            new_den = self.den
        return Fraction(new_num,new_den)

    #return fraction with number raised to the power
    def __pow__(self,power):
        new_num = self.num ** power
        new_den = self.den ** power
        return Fraction(new_num,new_den)

    #return fraction subtracted by the number other
    def __sub__(self,other):
        new_num = self.num*other.den - self.den*other.num
        new_den = self.num*other.num
        common = self.gdc(new_num,new_den)
        return Fraction(new_num // common, new_den // common)

    #return the division between 2 numbers with simplication
    def __truediv__(self,other):
        new_num = self.num*other.den
        new_den = self.den*other.num
        common = self.gdc(new_num, new_den)
        return Fraction(new_num // common ,new_den // common)

    #return fraction with operation xor between 2 numbers
    def __xor__(self,other):
        new_num = self.num ^ other.num
        new_den = self.den ^ other.den
        return Fraction(new_num,new_den)

    #print the fraction
    def show(self):
        print self.num,"/",self.den

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
        result = Fraction(-1,2)
        self.assertEqual(test,result)

    def teste_le(self):
        test = Fraction(1,2)
        other = Fraction(1,3)
        self.assertEqual(test <= other,False)

    def teste_lt(self):
        test = Fraction(1,2)
        other = Fraction(1,3)
        self.assertEqual(other < test,False)

    def teste_mul(self):
        test = Fraction(1,2)
        other = Fraction(1,3)
        result = Fraction(1,6)
        self.assertEqual(test * other,result)

    def teste_ne(self):
        test = Fraction(1,2)
        other = Fraction(1,3)
        self.assertEqual(test != other,True)

    def teste_neg(self):
        test = Fraction(1,2)
        result = Fraction(-1,2)
        self.assertEqual(-test,result)


if __name__ == "__main__":

    unittest.main()
