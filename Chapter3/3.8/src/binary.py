#!/usr/bin/py
#solved by FabioLima
#
#NameScript:	binary.py
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
import os,sys
sys.path.append(os.path.abspath('../../3.5/src/'))
from stack import Stack

class Stack(Stack):
    def divideBy2(self,number):
        test = Stack()
        while number > 0:
            if (number / 2) == 1:
                stack.push(1)
            else:
                stack.push(0)
            number /= 2
        seqBin = ''
        while not test.isEmpty():
            seq = seq + test.pop()
        return seqBin
