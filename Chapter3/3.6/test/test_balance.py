#!/usr/bin/py
#solved by FabioLima
#
#NameScript:	test_balance.py
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

	def test_checkBalance(self):
		test = Stack()
		self.assertTrue(test.verifyPar('()'))

if __name__ == "__main__":
	unittest.main()
