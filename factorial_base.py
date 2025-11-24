import pytest
from functools import cache

def factorial_iter(n):
    resultant = 1
    for i in range(2, n + 1):
        resultant *= i
    return resultant

def factorial_recursive(n):
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)

def run_tests(factorial):
    assert factorial(1) == 1
    assert factorial(0) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800

run_tests(factorial_recursive)
run_tests(factorial_iter)
