class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        divisors = set()
        for i in range(2, math.isqrt(num)):
            if num % i == 0:
                divisors.add(i)
                divisors.add(num // i)
        return sum(divisors) == num
