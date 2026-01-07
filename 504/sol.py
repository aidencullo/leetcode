class Solution:
    def convertToBase7(self, num: int) -> str:
        x = num
        digits = []

        while x:
            x, digit = divmod(x, 7)
            print(x, digit)
            digits.append(digit)

        digits.reverse()
        return ''.join(str(digit) for digit in digits)
