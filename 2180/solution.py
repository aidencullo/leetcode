class Solution:
    def countEven(self, num: int) -> int:
        def has_even_digits(n):
            total = 0
            while n:
                total += n % 10
                n //= 10
            return total % 2 == 0

        total = 0
        for i in range(1, num + 1):
            if has_even_digits(i):
                total += 1
        return total
