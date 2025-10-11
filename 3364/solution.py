class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        import math
        minimum_sum = math.inf
        for i in range(n):
            for j in range(i, n):
                subarray = nums[i: j + 1]
                m = len(subarray)
                m_sum = sum(subarray)
                if m >= l and m <= r and m_sum > 0:
                    minimum_sum = min(minimum_sum, m_sum)
        return minimum_sum if minimum_sum != math.inf else -1
