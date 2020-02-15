# -*- coding: utf-8 -*-
""" This program includes some iterating methods such as
    counting vowels, finding the last occurance and
    a generator without using built-in enumerate()

    author: Fatih IZGI
    date: 15-Feb-2020
    version: python 3.6.9
"""

import random
import unittest
from typing import Any, List, Optional, Sequence, Iterator


def count_vowels(s: str) -> int:
    """ return the number of vowels in the string s """

    vowel_count: int = 0
    s_lower: str = s.lower() # convert to lowercase

    for char in s_lower:
        if char in ['a', 'e', 'i', 'o', 'u']:
            vowel_count +=1 # if the char is vowel, increase the counter

    return vowel_count


def find_last(target: Any, seq: Sequence[Any]) -> Optional[int]:
    """ return the offset from 0 of the last occurrence of target in seq """

    try:
        index: Optional[int] = seq.index(target) # trying to find the first occurance
    except ValueError:  # cannot find any target in the sequence
        return None

    while True: # if one occurance is found, continue to search until the last occurance
        sub_seq: Sequence[Any] = seq[index+1:]      # create a subsequence starting from the found index+1
                                                    # to search the target in the new sequence
        try:
            new_index: int = sub_seq.index(target)  # if a new occurance is found
            index += new_index + 1                  # update the index
        except ValueError:                          # if cannot find any other target in the sequence
            break                                   # the last occurrence is already found, stop searching

    return index


def my_enumerate(seq: Sequence[Any]) -> Iterator[Any]:
    """ emulate the behavior of Python's built in enumerate() function.
        For each call, return a tuple with the offset from 0 and the next item
    """
    for (offset, value) in zip(range(len(seq)), seq):
        yield offset, value
