class Solution:
    def convertToBase7(self, num: int) -> str:
        """
        LeetCode 504: Base 7
        Given an integer num, convert it to a base 7 string.
        """
        if num == 0:
            return "0"
        
        x = num if num > 0 else -num
        digits = []

        while x:
            x, digit = divmod(x, 7)
            digits.append(digit)

        digits.reverse()
        base_7_str = ''.join(str(digit) for digit in digits)
        return base_7_str if num > 0 else '-' + base_7_str
    
