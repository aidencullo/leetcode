class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_sum = [1] + list(accumulate(nums, operator.mul))[:-1]
        right_sum = list(reversed(accumulate(reversed(nums), operator.mul)))[1:] + [1]
        return list(map(add, left_sum, right_sum))
