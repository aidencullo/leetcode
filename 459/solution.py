class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def is_repeating(sub, s):
            k = len(substr)
            if s % k != 0:
                
            
            return sub * (s // len(substr))

        
        for i in range(len(s) // 2):
            substr = s[:i + 1]
            if is_repeating(substr, s):
                return True
        return False
            
