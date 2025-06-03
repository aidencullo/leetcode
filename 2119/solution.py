class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        def reverse(s):
            s = str(s)
            s = s[::-1]
            s = int(s)
            return s

        return reverse(reverse(num)) == num
