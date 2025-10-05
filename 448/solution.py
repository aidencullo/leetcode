class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i, x in enumerate(nums):
            ind = abs(x) - 1
            nums[ind] = -abs(nums[ind])

        return [i + 1 for i, num in enumerate(nums) if num > 0]
