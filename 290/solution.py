from collections import Counter


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        return self.isIsomorphic(pattern, s.split())

    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return len(set(s)) == len(set(zip(s, t))) == len(set(t))
