#!/usr/bin/py

import unittest, os, sys
sys.path.append(os.path.abspath('..'))
from src.stack import Stack

class TestMethods(unittest.TestCase):

	def test_init(self):
		test = Stack()
		self.assertNotEqual(Stack(),test)

	def test_is_empty(self):
		test = Stack()
		self.assertTrue(test.isEmpty())

	def test_push(self):
		test = Stack()
		self.assertEqual(None,test.push(1))

	def test_pop(self):
		test = Stack()
		test.push('a')
		self.assertEqual('a',test.pop())
		
	def test_peek(self):
		test = Stack()
		test.push('b')
		self.assertEqual('b',test.peek())

	def test_size(self):
		test = Stack()
		self.assertEqual(0,test.size())

	def test_revString(self):
		test = Stack()
		self.assertEqual(test.revString('abc'),'c b a')

if __name__ == "__main__":
	unittest.main()
