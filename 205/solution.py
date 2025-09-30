from collections import Counter

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        seen = {}
        seen_t = set()
        for x, y in zip(s, t):
            if x in seen:
                if y != seen[x]:
                    return False
            else:
                if y in seen_t:
                    return False
                seen[x] = y
            seen_t.add(y)
        return True
                    
