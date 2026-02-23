class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = -math.inf
        running_max = 1
        running_min = 1

        for num in nums:
            candidates = (num, num * running_max, num * running_min)
            running_min = min(candidates)
            running_max = max(candidates)
            max_prod = max(max_prod, running_max)

        return max_prod
