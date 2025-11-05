class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        chars = list(s)
        n = len(s)
        l, r = 0, n - 1
        while l < r:
            while l < r and not chars[l].isalpha():
                l += 1
            while l < r and not chars[r].isalpha():
                r -= 1
            chars[l], chars[r] =  chars[r], chars[l]
            l += 1
            r -= 1
        return ''.join(chars)
