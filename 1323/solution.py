class Solution:
    def maximum69Number (self, num: int) -> int:
        n = len(str(num))
        for i, digit in enumerate(str(num)):
            if digit == "6":
                return num + 3 * 10 ** (n - 1 - i)
        return num
