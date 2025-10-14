class Solution:
    def validPalindrome(self, s: str) -> bool:

        def isPalindrome(s):
            for i in range(len(s) // 2):
                if s[i] != s[len(s) - 1 - i]:
                    return False
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return isPalindrome(s[l: r]) or isPalindrome(s[l + 1: r + 1])
            l += 1
            r -= 1
        return True
