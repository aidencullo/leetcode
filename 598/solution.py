class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        M = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                for a, b in ops:
                    if r < a and c < b:
                        M[r][c] += 1
        all_data = [item for row in M for item in row]
        max_item = max(all_data)
        return all_data.count(max_item)
                        
