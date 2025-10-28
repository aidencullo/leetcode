class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        others = {v: i for i, v in enumerate(nums)}
        for i, num in enumerate(nums):
            pair = target - num
            if pair in others and others[pair] != i:
                return [i, others[pair]]
