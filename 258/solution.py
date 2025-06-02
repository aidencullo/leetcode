class Solution:
    def addDigits(self, num: int) -> int:
        total = 0
        while num:
            total += num % 10
            num //= 10
        if total < 10:
            return total
        else:
            return self.addDigits(total)
