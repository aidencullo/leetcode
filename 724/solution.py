class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        def get_left_sum(index):
            if i == 0:
                return 0
            return left_prefix[index - 1]

        def get_right_sum(index):
            if i == n - 1:
                return 0
            return right_prefix[index + 1]
        
        if len(nums) == 1:
            return 0
        
        from itertools import accumulate
        left_prefix = list(accumulate(nums))
        total_sum = sum(nums)
        n = len(nums)
        right_prefix = [total_sum - left_prefix[i] + nums[i] for i in range(n)]
        for i in range(n):
            if get_left_sum(i) == get_right_sum(i):
                return i
        return -1
