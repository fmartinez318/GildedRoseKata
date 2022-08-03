# -*- coding: utf-8 -*-
import unittest

from fizzbuzz import FizzBuzz


class FizzBuzzTest(unittest.TestCase):

    def test_foo(self):
        fizzbuzz = FizzBuzz()
        self.assertEquals(fizzbuzz.print(0), "Foo")

        
if __name__ == '__main__':
    unittest.main()
