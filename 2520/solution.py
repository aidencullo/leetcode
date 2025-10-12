class Solution:
    def countDigits(self, num: int) -> int:
        x = num
        divisible_digits = 0
        while x:
            digit = x % 10
            if num % digit == 0:
                divisible_digits += 1
            x //= 10
        
        return divisible_digits
