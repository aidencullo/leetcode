import math

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        last_count, count = 0, 0
        i = 0
        substrings = 0
        while i < len(s):
            current = s[i]
            while i < len(s) and s[i] == current:
                count += 1
                i += 1
            substrings += min(count, last_count)
            last_count, count = count, 0
        return substrings
