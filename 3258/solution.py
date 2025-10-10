class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:

        def is_k_constrained(ones, zeroes, threshold):
            return ones <= threshold or zeroes <= threshold
        
        n = len(s)
        total_substrings = (n  * (n + 1)) // 2
        not_k_constraint_substrings = 0
        zeroes = 0
        ones = 0
        l = 0
        for i, c in enumerate(s):
            if c == '0':
                zeroes += 1
            else:
                ones += 1
            while not is_k_constrained(ones, zeroes, k):
                not_k_constraint_substrings += n - i
                if s[l] == '0':
                    zeroes -= 1
                else:
                    ones -= 1
                l += 1
        return total_substrings - not_k_constraint_substrings
