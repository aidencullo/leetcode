class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m * n
        min_cols = min(m, min(a for a, b in ops))
        min_rows = min(n, min(b for a, b in ops))
        return min_cols * min_rows
