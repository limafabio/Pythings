#!/usr/bin/py

# name file: Fraction.py
#
#Author: Fabio Lima
#Version 1 08/07/2016
#GPL License
#---------------------
#It's a Fraction class with a binary operators with test in the main

class Fraction:

    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def gdc(self,m,n):
        while m%n != 0:
            old_m = m
            old_n = n

            m = old_n
            n = old_m % old_n
        return n

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

    def __add__(self,other_fraction):
        new_num = self.num*other_fraction.den + self.den*other_fraction.num
        new_den = self.den*other_fraction.den
        common = self.gdc(new_num,new_den)
        return Fraction(new_num // common ,new_den // common)

    def __and__(self,other):
        new_num = self.num & other.num
        new_den = self.den & other.den
        return Fraction(new_num,new_den)

    def __div__(self,other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        return Fraction(new_num,new_den)


    def __index__(self):
        interger = self.num / self.den
        rest = (self.num / self.den) // 1
        if (rest < 0.6):
            return  (interger - rest)
        else:
            return (interger - rest + 1)

    def __invert__(self):
        return Fraction(~self.num,~self.den)

    def __mul__(self,other):
        new_den = self.num * other.num
        new_num = self.den * other.den
        return Fraction(new_den,new_num)

    def __neg__(self,other):
        return Fraction(-self.num,self.den)

    def __pow__(self,power):
        new_num = self.num ** power
        new_den = self.den ** power
        return Fraction(new_num,new_den)

    def __eq__(self,other):
        first_num = self.num *other.den
        second_num = other.num * self.den
        return first_num == second_num

    def show(self):
        print self.num,"/",self.den

if __name__ == "__main__":
    f1 = Fraction(1,2)
    f1.show()
    f2 = Fraction(1,2)
    print f1 + f2
    print f1 == f2
    f3 = Fraction(-1,3)
    print abs(f3)
    print f2 & f3
