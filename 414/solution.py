class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first_max = max(nums)
        second_max = -math.inf
        third_max = -math.inf
        for x in nums:
            if x != first_max:
                second_max = max(second_max, x)
        if second_max == -math.inf:
            return first_max
        for x in nums:
            if x != first_max and x != second_max:
                third_max = max(third_max, x)
        if third_max == -math.inf:
            return first_max
        return third_max
