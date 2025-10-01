class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            new_nums = nums[i:] + nums[:i]
            if sorted(new_nums) == new_nums:
                return True
        return False
