# LeetCode Problem 373: Find K Pairs with Smallest Sums
# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

from typing import List

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """
        You are given two integer arrays nums1 and nums2 sorted in non-decreasing order.
        Define a pair (u, v) which consists of one element from nums1 and one element from nums2.
        
        Return the k pairs (u, v) with the smallest sums.
        
        Args:
            nums1: First sorted array
            nums2: Second sorted array
            k: Number of pairs to return
            
        Returns:
            List of k pairs with smallest sums
        """
        pass


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    nums1_1 = [1,7,11]
    nums2_1 = [2,4,6]
    k1 = 3
    print(f"Example 1: {sol.kSmallestPairs(nums1_1, nums2_1, k1)}")  # Expected: [[1,2],[1,4],[1,6]]
    
    # Example 2
    nums1_2 = [1,1,2]
    nums2_2 = [1,2,3]
    k2 = 2
    print(f"Example 2: {sol.kSmallestPairs(nums1_2, nums2_2, k2)}")  # Expected: [[1,1],[1,1]]
