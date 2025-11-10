class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        acc = list(accumulate(nums))
        from bisect import bisect_right
        i = bisect_right(acc, sum(nums) / 2)
        return nums[:i + 1]
        
