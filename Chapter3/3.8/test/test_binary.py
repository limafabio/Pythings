#!/usr/bin/py
#solved by FabioLima
#
#NameScript:	test_binary.py
#
#Author and Maintaining: Fabio Lima
#
#-----------------------------------
#Description:
#
#
#-----------------------------------
#
#Example:
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
import src.binary from Stack

class TestMethods(unittest.TestCase):

    def testBigNumber(self):
        test = Stack()
        self.assertEqual(test.divideBy2(127),'1111111')

    def testSmallNumber(self):
        test = Stack()
        self.assertEqual(test.divideBy2(1),'1')

    def testSmallNumber(self):
        test = Stack()
        self.assertEqual(test.divideBy2(2),'10')

if __name__ == "__main__":
    unittest.main()
