# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 16:17:04 2026

@author: stu
"""

def is_even (i) :
    """
    Input : i, a positive int
    Returns True If i is even, otherwise false
    """
    return i % 2 == 0
print(is_even(3))
print(is_even(8))
my_function = is_even
print(my_function(4))