#!/usr/bin/python
#-*- coding: UTF-8 -*-

import unittest

def fun(x):
    return x + 1

class MyTest(unittest.TestCase):
    def test_func(self):
        self.assertEqual(fun(3), 4)

if __name__ == '__main__':
    unittest.main()
