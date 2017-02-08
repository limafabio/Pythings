#!/usr/bin/py
#solved by FabioLima
#
#NameScript:	test_symbols.py
#
#Author and Maintaining: Fabio Lima
#
#-----------------------------------
#Description: Test unity for method check symbols
#
#-----------------------------------
#
#Example: python test_symbols.py
#
#
#-----------------------------------
#
#History
#
#v1.0 2017/02/07, FabioLima
#
#-----------------------------------
#
#License: GPL
#

import unittest,os,sys
sys.path.append(os.path.abspath('..'))
from src.symbols import Stack

class TestMethods(unittest.TestCase):

	def testCheckSymbol1(self):
		test = Stack()
		self.assertTrue(test.checkSymbol('{{([][])}()}'))

	def testCheckSymbol2(self):
		test = Stack()
		self.assertTrue(test.checkSymbol('[][][](){}'))
	
	def testCheckSymbol3(self):
		test = Stack()
		self.assertFalse(test.checkSymbol('([)]'))

	def testCheckSymbol4(self):
		test = Stack()
		self.assertFalse(test.checkSymbol('[{()]'))

if __name__ == "__main__":
	unittest.main()
