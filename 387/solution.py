class Solution:
    def firstUniqChar(self, s: str) -> int:
        common = set()
        seen = set()
        for c in s:
            if c in seen:
                common.add(c)
            seen.add(c)
        for i, c in enumerate(s):
            if c not in common:
                return i
        return -1

