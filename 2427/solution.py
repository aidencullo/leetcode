import math

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        factors = set()
        for x in range(1, math.ceil(math.sqrt(a)) + 1):
            if a % x == 0:
                y = a // x
                if b % x == 0:
                    factors.add(x)
                if b % y == 0:
                    factors.add(y)
        return len(factors)
