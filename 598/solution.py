class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_cols = n
        min_rows = m
        for a, b in ops:
            min_cols = min(min_cols, b)
            min_rows = min(min_rows, a)
        return min_cols * min_rows
