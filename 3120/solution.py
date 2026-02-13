class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lowers = {c for c in word if c.islower()}
        uppers = {c for c in word if c.isupper()}
        uppers_lowered = {c.lower() for c in uppers}
        return len(lowers & uppers_lowered)
