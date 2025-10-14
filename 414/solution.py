class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums) < 3:
            return max(nums)
        first_max = max(nums)
        second_max = -math.inf
        third_max = -math.inf
        for x in nums:
            if x != first_max:
                second_max = max(second_max, x)
        for x in nums:
            if x != first_max and x != second_max:
                third_max = max(third_max, x)
        return third_max
