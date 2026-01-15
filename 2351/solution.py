class Solution:
    def repeatedCharacter(self, s: str) -> str:
        chars = defaultdict(int)
        
        for c in s:
            chars[c] += 1
            if chars[c] == 2:
                return c
