class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)
        good_substrings = 0
        for i in range(n - 2):
            if len(set(s[i: i + 3])) == 3:
                good_substrings += 1
        return good_substrings
