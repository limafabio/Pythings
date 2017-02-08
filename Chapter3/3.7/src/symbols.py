#!/usr/bin/py
#solved by FabioLima
#
#NameScript:	symbols.py
#
#Author and Maintaining: Fabio Lima
#
#-----------------------------------
#Description: Extension of stack class for check the simbols {[()]}
#
#-----------------------------------
#
#Example: python symbols.py
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

import sys,os
sys.path.append(os.path.abspath('../../3.5/src/'))
from stack import Stack

class Stack(Stack):

	def checkPair(self,char):
		pair = self.pop()

		if char == ']' and pair == '[':
			return True
		elif char == '}' and pair == '{':
			return True
		elif char == ')' and pair == '(':
			return True
		else:
			return False
		

	def checkSymbol(self,symbol):
		balanced = True
		for char in symbol:
			if not balanced:
				return False
			if char in '[{(':
				self.push(char)
			elif char in ']})' and self.isEmpty():
				balanced = False
			elif not char in ']})' or not self.checkPair(char):
				balanced = False
				
		return self.isEmpty()

