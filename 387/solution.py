class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = set()
        unique = set()

        for c in s:
            if c not in seen:
                unique.add(c)
            else:
                unique.discard(c)
            seen.add(c)
        

        for i, c in enumerate(s):
            if c in unique:
                return i
        return -1
        
