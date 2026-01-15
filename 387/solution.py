class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = set()
        uniq = set()
        chars = set(s)

        uniq |= chars

        for c in s:
            if c in seen:
                uniq.discard(c)
            seen.add(c)

        for i, c in enumerate(s):
            if c in uniq:
                return i
        return -1
        
