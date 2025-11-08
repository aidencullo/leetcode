class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        running_sum = 0
        for i, x in enumerate(nums):
            if running_sum == total_sum - running_sum - x:
                return i
            running_sum += x
        return -1
