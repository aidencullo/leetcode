class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ops = 0
        prev = -math.inf

        for curr in nums:
            ops += max(0, prev - curr + 1)
            prev = max(prev + 1, curr)

        return ops
