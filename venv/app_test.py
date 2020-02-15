# -*- coding: utf-8 -*-
""" Implement a test class to test the methods
    counting vowels, finding the last occurance and
    a generator without using built-in enumerate()

    author: Fatih IZGI
    date: 15-Feb-2020
    version: python 3.6.9
"""

import random
import unittest
from typing import Iterator, List, Tuple
from app import count_vowels, find_last, my_enumerate


class CountVowelsTest(unittest.TestCase):
    def test_count_vowels(self):
        """ testing count vowels """
        self.assertEqual(count_vowels("sdfghcvbnmxz."), 0)
        self.assertEqual(count_vowels("This is a test string."), 5)
        self.assertEqual(count_vowels("One MoRe StriNg to TESt."), 7)
        self.assertEqual(count_vowels("FfFffFAAaAaTTtTiIiHHhHh."), 8)
        self.assertEqual(count_vowels("A new generation of see-through solar cell technology"
                                      "could soon be used to harvest the massive energy potential of"
                                      "building and car windows, cell phones as well as other objects"
                                      "with a transparent surface."), 64)


class FindLastTest(unittest.TestCase):
    def test_find_last(self) -> None:
        """ testing find_last """
        self.assertEqual(find_last("p", "This is a test string."), None)
        self.assertEqual(find_last("t", "This is a test string."), 16)
        self.assertEqual(find_last(".", "This is a test string."), 21)
        self.assertEqual(find_last("ng.", "This is a test string."), 19)
        self.assertEqual(find_last("This is a test string.", "This is a test string."), 0)
        self.assertEqual(find_last("is", "This is a test string."), 5)
        self.assertEqual(find_last("i", "This is a test string."), 18)
        self.assertEqual(find_last("uch", "Too much StriNg, too Much TESt."), 22)
        self.assertEqual(find_last("ghjk", "asdfghjklasdfghjkl"), 13)
        self.assertEqual(find_last(33, [42, 33, 21, 33]), 3)
        self.assertEqual(find_last(42, [42, 33, 21, 33]), 0)
        self.assertEqual(find_last(10, [42, 33, 21, 33]), None)


class EnumerateTest(unittest.TestCase):
    def test_enumerate_list(self) -> None:
        """ test my_enumerate by storing the results in a list """
        self.assertTrue(list(my_enumerate([0,1,2,3,4,5])) == list(enumerate([0,1,2,3,4,5])))
        self.assertTrue(list(my_enumerate("Test!")) == list(enumerate("Test!")))


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)