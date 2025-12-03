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


def time_fibo_once(fibo_impl, n):
    start = time()
    fibo_impl(n)
    print(f"{n} {time() - start:.15f}")
    # print(f"{n:.10f} {time() - start}")

def test_fibonacci_times(fibo_impl, max_n=30, step=10):
    for n in range(step, max_n + 1, step):
        start = time()
        fibo_impl(n)
        print(f"{n} {time() - start}")

# this fails on recursion depth limit
# test_fibonacci_times(fibo_cached, max_n=100000, step=1000)

#too long
# test_fibonacci_times(fibo_cached, max_n=100000, step=100)
# test_fibonacci_times(fibo)

fibo_cached.cache_clear()
time_fibo_once(fibo_cached, 100)
fibo_cached.cache_clear()
time_fibo_once(fibo_cached, 200)
fibo_cached.cache_clear()
time_fibo_once(fibo_cached, 300)
fibo_cached.cache_clear()
time_fibo_once(fibo_cached, 400)
fibo_cached.cache_clear()
time_fibo_once(fibo_cached, 500)


'''
not showing linear -- not sure what's going on


100 0.000060796737671
200 0.000340938568115
300 0.000891923904419
400 0.001120567321777
500 0.000471115112305
'''

