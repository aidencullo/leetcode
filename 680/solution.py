class Solution:
    def validPalindrome(self, s: str) -> bool:

        def isPalindromeLeft(s):
            different = False
            l = 0
            r = len(s) - 1
            while l < r:
                if s[l] != s[r] and different:
                    return False
                if s[l] != s[r]:
                    different = True
                    l += 1
                    continue
                l += 1
                r -= 1
            return True

        def isPalindromeRight(s):
            different = False
            l = 0
            r = len(s) - 1
            while l < r:
                if s[l] != s[r] and different:
                    return False
                if s[l] != s[r]:
                    different = True
                    r -= 1
                    continue
                l += 1
                r -= 1
            return True
                
        return isPalindromeLeft(s) or isPalindromeRight(s)
