import pytest

def factorial(n):
    if n < 0:
        raise Exception
    if n == 0:
        return 1
    return n * factorial(n - 1)

# normal asserts
assert factorial(1) == 1
assert factorial(0) == 1
assert factorial(5) == 120
assert factorial(10) == 3628800

# assert exception
with pytest.raises(Exception):
    factorial(-1)
