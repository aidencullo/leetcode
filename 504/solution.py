class Solution:
    def convertToBase7(self, num: int) -> str:
        """
        LeetCode 504: Base 7
        Given an integer num, convert it to a base 7 string.
        """
        x = num
        digits = []

        while x:
            x, digit = divmod(x, 7)
            digits.append(digit)

        digits.reverse()
        return ''.join(str(digit) for digit in digits)
