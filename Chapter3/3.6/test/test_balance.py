#!/usr/bin/py
#solved by FabioLima
#
#NameScript:	test_balance.py
#
#Author and Maintaining: Fabio Lima
#
#-----------------------------------
#Description: just simple test with balance class,
#that is a extension of stack class in folder 3.5
#
#-----------------------------------
#
#Example: python test_balance.py
#
#
#-----------------------------------
#
#History
#
#v1.0 2017/02/04, FabioLima
#
#-----------------------------------
#
#License: GPL
#
import os,sys,unittest
sys.path.append(os.path.abspath('..'))
from src.balance import Stack

class TestMethods(unittest.TestCase):

	def test_checkBalanceTrue(self):
		test = Stack()
		self.assertTrue(test.verifyPar('()'))

	def test_checkBalanceFalse1(self):
		test = Stack()
		self.assertFalse(test.verifyPar(')('))
	
	def test_checkBalanceFalse2(self):
		test = Stack()
		self.assertFalse(test.verifyPar('(('))

if __name__ == "__main__":
	unittest.main()
