class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l, r = 0, 0
        from collections import Counter
        counter = Counter()
        n = len(s)
        longest = 0
        while r < n:
            while r < n and (not counter or max(counter.values()) <= 2):
                counter[s[r]] += 1
                r += 1
            longest = max(longest, r - l)
            if r == n:
                return longest
            while max(counter.values()) == 3:
                counter[s[l]] -= 1
                l += 1
        return longest
            
