class Solution:
    def countElements(self, nums: List[int]) -> int:
        return sum(min(nums) < x < max(nums) for x in nums)
