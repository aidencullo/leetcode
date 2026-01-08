class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, 0
        n = len(nums)

        while r < n:
            while r < n - 1 and nums[r] == 0:
                r += 1
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r += 1
