class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = set()
        seen_more = set()

        for c in s:
            if c in seen:
                seen_more.add(c)
            seen.add(c)

        all_chars = set(s)
        all_chars -= seen_more

        for i, c in enumerate(s):
            if c in all_chars:
                return i
        return -1
        
