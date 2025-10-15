class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        ones = 0
        for x in nums:
            if x == 1:
                ones += 1
            else:
                ones = 0
            max_ones = max(max_ones, ones)
        return max_ones
