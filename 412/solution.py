def is_int(x):
    return isinstance(x, int)

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        def buzz(x):
            if not is_int(x):
                return x
            if x % 5 == 0:
                return "Buzz"
            return x

        def fizz(x):
            if not is_int(x):
                return x
            if x % 3 == 0:
                return "Fizz"
            return x


        def fizz_buzz(x):
            if not is_int(x):
                return x
            if x % 3 == 0 and x % 5 == 0:
                return "FizzBuzz"
            return x

        
        fizz_buzzed = map(fizz_buzz, range(1, n + 1))
        fizz_processed = map(fizz, fizz_buzzed)
        buzz_processed = map(buzz, fizz_processed)
        result = list(map(str, buzz_processed))
        
        return result
