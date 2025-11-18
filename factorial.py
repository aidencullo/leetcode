import time
# from decorators import timer
import sys
sys.setrecursionlimit(10**5)  # default ~1000


def factorial(n):
    if n < 0:
        raise Exception
    if n == 0:
        return 1
    return n * factorial(n - 1)

assert factorial(1) == 1
assert factorial(0) == 1
assert factorial(5) == 120
assert factorial(10) == 3628800


def timed_factorial(n):

    for i in range(5):
        n = 10 ** i
        start = time.time()
        result = factorial(n)
        end = time.time()
        print(f'n={n:<10}: {end - start:>10.6f}s')

def timer(fn):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fn(*args, **kwargs)
        end = time.time()
        print(f'{end - start}s')
        return result
    return wrapper

timed = timer(factorial)
timed(1)
