class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        min_sum = math.inf
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    left = nums[i]
                    middle = nums[j]
                    right = nums[k]
                    if left < middle and right < middle:
                        min_sum = min(min_sum, left + middle + right)
        return min_sum if min_sum != math.inf else -1
