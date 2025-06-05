class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        counts = Counter(s)
        counts = [key for key, value in counts.items() if value == 1]
        if not counts:
            return -1
        return s.index(counts[0])
