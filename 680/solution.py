class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s):
            for i in range(len(s) // 2):
                if s[i] != s[len(s) - i - 1]:
                    return False
            return True

        if isPalindrome(s):
            return True

        for i in range(len(s)):
            new_s = s[:i] + s[i + 1:]
            if isPalindrome(new_s):
                return True
        return False
