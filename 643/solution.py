class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l, r = 0, k
        n = len(nums)
        max_avg = float('-inf')
        current = sum(nums[:k])
        max_avg = max(max_avg, current / k)
        while r < n:
            current -= nums[l]
            current += nums[r]
            max_avg = max(max_avg, current / k)
            l += 1
            r += 1
        return max_avg
