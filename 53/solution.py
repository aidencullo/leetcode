class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = -math.inf
        running = 0
        for num in nums:
            running += num
            max_sum = max(max_sum, running)

            if running < 0:
                running = 0

        return max_sum
