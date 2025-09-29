class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        def buzz(x):
            if not isinstance(x, int):
                return x
            if x % 5 == 0:
                return "Buzz"
            return x

        def fizz(x):
            if not isinstance(x, int):
                return x
            if x % 3 == 0:
                return "Fizz"
            return x


        def fizz_buzz(x):
            if not isinstance(x, int):
                return x
            if x % 3 == 0 and x % 5 == 0:
                return "FizzBuzz"
            return x

        
        fizzBuzzed = list(map(str, map(buzz, map(fizz, map(fizz_buzz, range(1, n + 1))))))
        return fizzBuzzed
