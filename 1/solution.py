class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        others = {}
        for i, num in enumerate(nums):
            pair = target - num
            if pair in others:
                return [i, others[pair]]
            others[num] = i
