class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        from collections import deque

        seen = set()
        directions = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
        n = len(grid)
        q = deque()
        q.appendleft((0, 0, 1))

        while q:
            r, c, dist = q.pop()
            if not (0 <= r < n and 0 <= c < n and (r, c) not in seen and not grid[r][c]):
                continue
            seen.add((r, c))
            if r == c == n - 1:
                return dist

            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                q.appendleft((new_r, new_c, dist + 1))
        return -1
