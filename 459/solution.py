class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def is_repeating(sub, s):
            k = len(substr)
            n = len(s)
            if n % k != 0:
                return False
            return sub * (n // k) == s

        
        for i in range(len(s) // 2):
            substr = s[:i + 1]
            if is_repeating(substr, s):
                return True
        return False
            
