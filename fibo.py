from functools import cache
from time import time

@cache
def fibo_cached(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo_cached(n - 1) + fibo_cached(n - 2)

def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n - 1) + fibo(n - 2)


def test_fibonacci_times(fibo_impl, max_n=30, step=10):
    for n in range(step, max_n + 1, step):
        start = time()
        fibo_impl(n)
        print(f"{n} {time() - start}")

test_fibonacci_times(fibo_cached, max_n=100000, step=1000)
test_fibonacci_times(fibo)
