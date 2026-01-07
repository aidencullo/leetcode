# LeetCode Problem 64: Minimum Path Sum
# https://leetcode.com/problems/minimum-path-sum/

class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        """
        Given a m x n grid filled with non-negative numbers,
        find a path from top left to bottom right which minimizes the sum of all numbers along its path.
        
        Note: You can only move either down or right at any point in time.
        
        Args:
            grid: m x n grid of non-negative integers
            
        Returns:
            The minimum sum path from top-left to bottom-right
        """
        def dfs(r, c, last):

            nonlocal path

            if not (0 <= r < rows and 0 <= c < cols):
                return

            val = grid[r][c]
            current = last + val

            if r == rows - 1 and c == cols - 1:
                path = min(current, path)

            dfs(r, c + 1, current)
            dfs(r + 1, c, current)

            
                
        rows, cols = len(grid), len(grid[0])
        path = math.inf
        dfs(0, 0, 0)
        return path
