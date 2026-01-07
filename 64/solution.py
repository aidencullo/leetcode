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
        pass


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    grid1 = [[1,3,1],[1,5,1],[4,2,1]]
    print(f"Example 1: {sol.minPathSum(grid1)}")  # Expected: 7
    
    # Example 2
    grid2 = [[1,2,3],[4,5,6]]
    print(f"Example 2: {sol.minPathSum(grid2)}")  # Expected: 12
