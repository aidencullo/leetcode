from functools import wraps

def my_decorator(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print("Before")
        result = fn(*args, **kwargs)
        print("After")
        return result
    return wrapper

@my_decorator
def greet(name):
    """Say hello to someone."""
    return f"Hello, {name}!"

print(greet("Alice"))
print(greet.__name__)  # 'greet', not 'wrapper'
print(greet.__doc__)   # 'Say hello to someone.'
