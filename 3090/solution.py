class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        from collections import Counter
        counter = Counter()
        n = len(s)
        longest = 0
        l, r = 0, -1
        while r < n:
            while r < n and (not counter or max(counter.values()) < 3):
                longest = max(longest, r - l + 1)                
                r += 1
                if r == n:
                    return longest
                counter[s[r]] += 1
            while max(counter.values()) == 3:
                counter[s[l]] -= 1
                l += 1
        return longest
            
