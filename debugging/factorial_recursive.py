#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    Calculate the factorial of a given non-negative integer using recursion.
    The factorial of n (n!) is the product of all positive integers less than 
    or equal to n. The base case handles 0, where 0! is defined as 1.

    Parameters:
    n (int): The non-negative integer to compute the factorial for.

    Returns:
    int: The computed factorial value of the integer n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        f = factorial(int(sys.argv[1]))
        print(f)
