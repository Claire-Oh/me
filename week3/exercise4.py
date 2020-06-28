# -*- coding: UTF-8 -*-
"""Week 3, Exercise 4."""


import math
# import time


def binary_search(low, high, actual_number):
    """Do a binary search.

    This is going to be your first 'algorithm' in the usual sense of the word!
    you'll give it a range to guess inside, and then use binary search to home
    in on the actual_number.
    
    Each guess, print what the guess is. Then when you find the number return
    the number of guesses it took to get there and the actual number
    as a dictionary. make sure that it has exactly these keys:
    {"guess": guess, "tries": tries}
    
    This will be quite hard, especially hard if you don't have a good diagram!
    
    Use the VS Code debugging tools a lot here. It'll make understanding 
    things much easier.
    """
    
def binary_search(low, high, actual_number):
    A = list(range(low, high + 1))
    dict = {"guess": actual_number, "tries": 0}
    found = do_binary_search(A, low - 1, high - 1, actual_number, dict)
    print(found)
    return dict


def do_binary_search(A, l, h, k, dict):
    dict["tries"] = dict["tries"] + 1 
    if h >= l:
        mid = l + (h - l) // 2
        print("trying " + str(A[mid])) 
        if A[mid] == k:
            dict["tries"] = dict["tries"] - 1 
            return str(k) + ' is found'
        elif A[mid] > k:
            return do_binary_search(A, l, mid-1, k, dict)
        else:
            return do_binary_search(A, mid+1, h, k, dict)
    else:
        return str(k) + ' is not found'


if __name__ == "__main__":
    print(binary_search(1, 100, 5))
    print(binary_search(1, 100, 6))
    print(binary_search(1, 100, 95))
    print(binary_search(1, 51, 5))
    print(binary_search(1, 50, 5))
