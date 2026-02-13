class Solution:
    def greatestLetter(self, s: str) -> str:
        greatest = ""
        letters = set(s)
        for c in s:
            if c.isupper() and c.lower() in letters:
                greatest = max(c, greatest)
        return greatest
