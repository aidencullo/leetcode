class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        from collections import Counter
        if len(s1) != len(s2):
            return False
        diffs = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diffs.append(i)
        count = len(diffs)
        if count == 0:
            return True
        if count == 2:
            return s1[diffs[0]] == s2[diffs[1]] and s1[diffs[1]] == s2[diffs[0]]
        return False
        
