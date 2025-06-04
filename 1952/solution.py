class Solution:
    def isThree(self, n: int) -> bool:
        def countDivisors(x):
            divisors = set((1, x))
            for i in range(2, int(math.sqrt(x)) + 1):
                if x % i == 0:
                    divisors.add(i)
                    divisors.add(x // i)
            return len(divisors)

        return countDivisors(n) == 3
