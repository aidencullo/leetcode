class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        def is_strong(x, y):
            return abs(x - y) <= min(x, y)
        
        n = len(nums)
        xor = 0
        for x in nums:
            for y in nums:
                if is_strong(x, y):
                    xor = max(xor, x ^ y)
        return xor
