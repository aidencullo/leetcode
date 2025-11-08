class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_prefix_sum = 0
        right_prefix_sum = sum(nums)
        for i, x in enumerate(nums):
            right_prefix_sum -= x
            if left_prefix_sum == right_prefix_sum:
                return i
            left_prefix_sum += x
        return -1
