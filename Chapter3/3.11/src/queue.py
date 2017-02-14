#!/usr/bin/py
#solved by FabioLima
#
#NameScript:	queue.py
#
#Author and Maintaining: Fabio Lima
#
#-----------------------------------
#Description: class with queue operations 
#
#
#-----------------------------------
#
#Example: python queue.py
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

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self,item):
        self.items.insert(0,item)

    def size(self):
        return len(self.items)

    def dequeue(self):
        return self.items.pop()



