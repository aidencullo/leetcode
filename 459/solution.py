class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def is_repeating(idx, s):
            k = idx + 1
            n = len(s)
            if n % k != 0:
                return False

            for j in range(n):
                if s[j % k] != s[j]:
                    return False
            return True

        
        for i in range(len(s) // 2):
            if is_repeating(i, s):
                return True
        return False
            
