#!/usr/bin/env python
"""Implements math functions without using operators except for '+' and '-' """

__author__ = "jsinghw"

import operator


def add(x, y):
    """Add two integers. Handles negative values."""
    return(x+y)


def multiply(x, y):
    """Multiply x with y. Handles negative values of x or y."""
    output = 0
    if x > 0 and y > 0:
        for i in range(0, y):
            output += x
        return output
    elif x < 0 and y > 0:
        for i in range(0, y):
            output += operator.neg(x)
        return operator.neg(output)
    elif x > 0 and y < 0:
        for i in range(0, operator.neg(y)):
            output += x
        return operator.neg(output)
    elif x < 0 and y < 0:
        for i in range(0, operator.neg(y)):
            output += operator.neg(x)
        return(output)


def power(x, n):
    """Raise x to power n, where n >= 0"""
    if n == 0:
        return(1)
    output = x
    for i in range(1, n):
        output = multiply(output, x)
    return(output)


def factorial(x):
    """Compute factorial of x, where x > 0"""
    if x == 1:
        return(1)
    output = 1
    for i in range(1, x+1):
        output = multiply(output, i)
    return(output)


def fibonacci(n):
    """Compute the nth term of fibonacci sequence"""
    total = 1
    temp1 = 0
    temp2 = 1
    for i in range(1, n):
        total = add(temp1, temp2)
        temp1 = temp2
        temp2 = total
    return(total)


if __name__ == '__main__':
    # your code to call functions above
    pass
    print(fibonacci(1))
    
    """Should be 81"""

