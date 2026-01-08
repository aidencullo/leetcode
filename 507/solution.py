class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        divisors = set()
        for i in range(1, math.isqrt(num) + 1):
            if num % i == 0:
                divisors.add(i)
                divisors.add(num // i)
        divisors.discard(num)
        return sum(divisors) == num
