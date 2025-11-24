import pytest
from functools import cache

@cache
def factorial_optimized(n):
    if n == 0:
        return 1
    return n * factorial_optimized(n - 1)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def run_tests():
    # normal asserts
    assert factorial(1) == 1
    assert factorial(0) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800

run_tests()
