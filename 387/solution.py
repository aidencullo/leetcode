class Solution:
    def firstUniqChar(self, s: str) -> int:
        repeat = set((Counter(s) - Counter(set(s))).keys())
        uniq = set(s) - repeat

        for i, c in enumerate(s):
            if c in uniq:
                return i
        return -1
        
