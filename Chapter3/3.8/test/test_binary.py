#!/usr/bin/py
#solved by FabioLima
#
#NameScript:	test_binary.py
#
#Author and Maintaining: Fabio Lima
#
#-----------------------------------
#Description: Test for 2 functions convert base
#
#
#-----------------------------------
#
#Example: python test_binary.py
#
#
#-----------------------------------
#
#History
#
#v1.0 2017/02/08, FabioLima
#
#-----------------------------------
#
#License: GPL
#
import unittest,os,sys
sys.path.append(os.path.abspath('..'))
from src.binary import Stack

class TestMethods(unittest.TestCase):

    def testBase2BigNumber(self):
        test = Stack()
        self.assertEqual(test.divideBy2(127),'1111111')

    def testBase2SmallNumber1(self):
        test = Stack()
        self.assertEqual(test.divideBy2(1),'1')

    def testBase2SmallNumber2(self):
        test = Stack()
        self.assertEqual(test.divideBy2(2),'10')

    def testBaseConvert1(self):
        test = Stack()
        self.assertEqual(test.baseConverter('25','8'),'31')

    def testBaseConvert2(self):
        test = Stack()
        self.assertEqual(test.baseConverter('256','16'),'100')

    def testBaseConvert3(self):
        test = Stack()
        self.assertEqual(test.baseConverter('26','26'),'10')

if __name__ == "__main__":
    unittest.main()
