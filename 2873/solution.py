class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        maximum_value = -math.inf
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    maximum_value = max((nums[i] - nums[j]) * nums[k], maximum_value)
        return maximum_value if maximum_value >= 0 else 0
