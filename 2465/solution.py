class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        averages = set()
        n = len(nums)
        for i in range(n):
            averages.add((nums[i] + nums[n - i - 1]) / 2)
        return len(averages)
