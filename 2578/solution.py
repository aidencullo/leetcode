class Solution:
    def splitNum(self, num: int) -> int:
        digits = [int(c) for c in str(num)]
        digits.sort(reverse=True)
        res = 0
        for i, digit in enumerate(digits):
            res += digit * 10 ** (i // 2)
        return res
