class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        k_constraint_substrings = 0
        for i in range(n):
            ones = 0
            zeroes = 0
            for j in range(i, n):
                if s[j] == '0':
                    zeroes += 1
                else:
                    ones += 1
                if ones <= k or zeroes <= k:
                    k_constraint_substrings += 1
        return k_constraint_substrings
