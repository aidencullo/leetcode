class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        min_sum = math.inf
        n = len(nums)
        prefix_sum_left = []
        prefix_sum_right = []
        minn = math.inf
        for num in nums:
            minn = min(minn, num)
            prefix_sum_left.append(minn)
        minn = math.inf
        for num in reversed(nums):
            minn = min(minn, num)
            prefix_sum_right.append(minn)
        prefix_sum_right = prefix_sum_right[::-1]
        for i in range(n):
            middle = nums[i]
            min_left = prefix_sum_left[i - 1] if i > 0 else math.inf
            min_right = prefix_sum_right[i + 1] if i < n - 1 else math.inf
            if min_left < middle and min_right < middle:
                min_sum = min(min_sum, min_left + middle + min_right)
        return min_sum if min_sum != math.inf else -1
