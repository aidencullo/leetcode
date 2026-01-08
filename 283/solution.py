class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        write = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                nums[write] = nums[i]
                write += 1

        for i in range(write, n):
            nums[i] = 0
        
