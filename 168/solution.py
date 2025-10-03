class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        n = columnNumber
        while n:
            n -= 1
            n, digit = divmod(n, 26)
            res += chr(65 + digit)
        return "".join(reversed(res))
