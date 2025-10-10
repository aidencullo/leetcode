class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:

        def is_k_constrained(ones, zeroes, threshold):
            return ones <= threshold or zeroes <= threshold

        def increment(ones, zeroes, c):
            if c == "0":
                zeroes += 1
            else:
                ones += 1
            return ones, zeroes

        def decrement(ones, zeroes, c):
            if c == "0":
                zeroes -= 1
            else:
                ones -= 1
            return ones, zeroes

        n = len(s)
        total_substrings = (n * (n + 1)) // 2
        not_k_constraint_substrings = 0
        zeroes = 0
        ones = 0
        left = 0
        for right, c in enumerate(s):
            ones, zeroes = increment(ones, zeroes, c)
            while not is_k_constrained(ones, zeroes, k):
                not_k_constraint_substrings += n - right
                ones, zeroes = decrement(ones, zeroes, s[left])
                left += 1
        return total_substrings - not_k_constraint_substrings
