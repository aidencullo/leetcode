from decorator import decorator
import time

@decorator
def timer(func, *args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    print(f"{func.__name__} took {time.time() - start:.4f}s")
    return result

@timer
def f(x):
    return sum(range(x))

f(1000000)
