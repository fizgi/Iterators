# -*- coding: utf-8 -*-
""" This program takes the first and last name from the user
    and prints a greeting message.

    author: Fatih IZGI
    date: 15-Feb-2020
    version: python 3.6.9
"""

import random
import unittest
from typing import Any, List, Optional, Sequence, Iterator


# PART 1

def count_vowels(s: str) -> int:
    """ return the number of vowels in the string s """

    vowel_count: int = 0
    s_lower: str = s.lower() # convert to lowercase

    for char in s_lower:
        if char in ['a', 'e', 'i', 'o', 'u']:
            vowel_count +=1 # if the char is vowel, increase the counter

    return vowel_count

# PART 2

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

# PART 3 is Fraction.simplify()

# PART 4
def my_enumerate(seq: Sequence[Any]) -> Iterator[Any]:
    """ emulate the behavior of Python's built in enumerate() function.
        For each call, return a tuple with the offset from 0 and the next item
    """
    for (offset, value) in zip(range(len(seq)), seq):
        yield offset, value

# PART 5

def generator(min_val: int, max_val: int) -> Iterator[int]:
    """ yield an infinite number of integers """
    # TODO: implement me
    yield 0  # replace with implementation


def find_target(target: int, min_val: int = 0, max_val: int = 10, max_attempts: int = 100) -> Optional[int]:
    """ Count the number of random values read before finding target """
    # TODO: implement me

    return None
