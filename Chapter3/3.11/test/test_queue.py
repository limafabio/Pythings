#!/usr/bin/py
#solved by FabioLima
#
#NameScript:	test_queue.py
#
#Author and Maintaining: Fabio Lima
#
#-----------------------------------
#Description: unittest for queue operations
#
#
#-----------------------------------
#
#Example: python test_queue.py
#
#
#-----------------------------------
#
#History
#
#v1.0 2017/02/14, FabioLima
#
#-----------------------------------
#
#License: GPL
#

import unittest,os,sys
sys.path.append(os.path.abspath('..'))
from src.queue import Queue

class TestMethods(unittest.TestCase):

    def test_init(self):
        test = Queue()
        self.assertNotEqual(Queue(),test)

    def test_is_empty(self):
        test = Queue()
        self.assertEqual(test.isEmpty(),True)
    
    def test_enqueue(self):
        test = Queue()
        test.enqueue(1)
        self.assertEqual(test.dequeue(),1)

    def test_dequeue(self):
        test = Queue()
        test.enqueue(1)
        test.dequeue()
        self.assertEqual(test.isEmpty(),True)

    def test_size(self):
        test = Queue()
        test.enqueue(1)
        self.assertEqual(test.size(),1)
if __name__ == "__main__":
    unittest.main()
