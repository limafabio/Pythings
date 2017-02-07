#!/usr/bin/py

#solved by FabioLima
#
#NameScript:	balance.py
#
#Author and Maintaining: Fabio Lima
#
#-----------------------------------
#Description: Just a simple checker for balanced parentheses 
#using class Stack in folder 3.5
#
#-----------------------------------
#
#Example: python balance.py
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
import sys,os
sys.path.append(os.path.abspath('../../3.5/src/'))
from stack import Stack

class Stack(Stack):
	def verifyPar(self,simbol):

		for par in simbol:
			if (par != ')' and par != '('):
				return False
			elif (par == ')' and self.isEmpty()):
				return False
			elif (par == '('):
				self.push('(')
			elif (par == ')' and (not self.isEmpty())):
				self.pop()

		return self.isEmpty()
