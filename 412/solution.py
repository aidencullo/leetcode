from functools import partial




class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        def buzz(x):
            try: 
                if x % 5 == 0:
                    return "Buzz"
            except:
                pass
            return x

        def fizz(x):
            try: 
                if x % 3 == 0:
                    return "Fizz"
            except:
                pass
            return x
 
        def fizz_buzz(x):
            return try_fn(fizz_buzz_inner, x)

        def fizz_buzz_inner(x):
            if x % 3 == 0 and x % 5 == 0:
                return "FizzBuzz"
            return x

        def try_fn(fn, x):
            try: 
                return fn(x)
            except:
                return x

        
        fizz_buzzed = map(fizz_buzz, range(1, n + 1))
        fizzed = map(fizz, fizz_buzzed)
        buzzed = map(buzz, fizzed)
        result = list(map(str, buzzed))
        
        return result
