class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        from collections import Counter

        counter = Counter()

        n = len(s)
        left = 0
        longest = 2
        for i in range(n):
            counter[s[i]] += 1
            while counter[s[i]] == 3:
                counter[s[left]] -= 1
                left += 1
            longest = max(longest, i - left + 1)
        return longest
