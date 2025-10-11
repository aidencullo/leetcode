class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        factors = 0
        for x in range(1, a + 1):
            if a % x == 0 and b % x == 0:
                factors += 1
        return factors
