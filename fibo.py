from functools import cache
from time import time

def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n - 1) + fibo(n - 2)

fibo_cached = cache(fibo)

def test_fibonacci_times(fibo_impl, max_n=30, step=10):
    for n in range(step, max_n + 1, step):
        start = time()
        fibo_impl(n)
        print(f"{n} {time() - start}")

test_fibonacci_times(fibo_cached)
test_fibonacci_times(fibo)
