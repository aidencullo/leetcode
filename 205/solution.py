from collections import Counter

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def isIsomorphic(s: str, t: str) -> bool:

            if len(s) != len(t):
                return False
            
            seen = {}
            for x, y in zip(s, t):
                if x in seen:
                    if y != seen[x]:
                        return False
                else:
                    seen[x] = y
            return True

        return isIsomorphic(s, t) and isIsomorphic(t, s)
    
