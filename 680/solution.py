class Solution:
    def validPalindrome(self, s: str) -> bool:

        def isPalindrome(start, end):
            length = end - start + 1
            iterations = length // 2
            for i in range(iterations):
                if s[start + i] != s[end - i]:
                    return False
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return isPalindrome(l + 1, r) or isPalindrome(l, r - 1)
            l += 1
            r -= 1
        return True
