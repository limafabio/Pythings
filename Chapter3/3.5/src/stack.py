#!/usr/bin/py

# name file: Stack.py
#
# Author: Fabio Lima
# Version 1 01/02/2017
# GPL License
# ---------------------
# Class Stack where the end of list is the top of stack
# There are basic operations for stack 


class Stack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		return self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		size = len(self.items)-1
		return self.items[size]

	def size(self):
		return len(self.items)

	def revString(self, elem):
		split = (elem)
		for char in split:
			self.push(char)

		answer = ''
		while not self.isEmpty():
			answer += self.peek()	
			self.pop()
		return answer
