#!/usr/bin/python3
"""
alx-interview: write a method that
calculates the fewest number of operations.

single char = H, operations(ops) = copyAll & paste,
n = number given, result = ?

Solution:

# initialize a variable for the total number of operations
and single_char to store the current number of H characters
in the file (initially 1, since we start with one H).

# while single_char is less than n:
    If n is divisible by H:
     perform All operations (n // H) times.
     Update H to be H * (n // H)(since we’ve added more H characters).
     increment operations by (n // H) (since we performed many operations).
# return the final value of operations
"""


def minOperations(n: int):
    """
    returns exactly n-H
    characters in the file.
    """
    ops = 0
    single_char = 1

    while single_char < n:
        if n % single_char == 0:
            ops += n // single_char
            single_char *= n // single_char
        else:
            return 0

    return ops
