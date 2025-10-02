class Solution:
    def check(self, nums: list[int]) -> bool:
        el = nums[0]
        pivot = 0
        for i, x in enumerate(nums):
            if x < el:
                pivot = i
                break
            el = x

        new_nums = nums[pivot:] + nums[:pivot]

        el = new_nums[0]
        for x in new_nums:
            if x < el:
                return False
            el = x
            
        return True
