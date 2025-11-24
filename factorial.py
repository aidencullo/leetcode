from factorial_base import factorial, factorial_optimized

import time
import sys

sys.setrecursionlimit(10**5)  # default ~1000

def time_fn_mult(fn):
    for i in range(5):
        n = 10 ** i
        time_fn(fn, n)

def time_fn(fn, n):
        start = time.time()
        result = fn(n)
        end = time.time()
        print(f'n={n:<10}: {end - start:>10.6f}s')

time_fn_mult(factorial)
time_fn_mult(factorial_optimized)
