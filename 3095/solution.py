import math

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:

        def subtract_bits(x):
            for i in range(32):
                shield  = 1 << i
                if shield & x:
                    bit_count[i] -= 1

        def add_bits(x):
            for i in range(32):
                shield  = 1 << i
                if shield & x:
                    bit_count[i] += 1

        def bits_to_dec():
            for i in range(32):
                bit = bit_count[i]
                bit

        bit_count = [0] * 32
        shortest = math.inf
        bitwise_or = 0
        for i in range(n):
            x = nums[i]
            add_bits(x)
            bitwise_or = bits_to_dec()
            while bitwise_or >= k:
                shortest = min(shortest, i - l + 1)
                subtract_bits(nums[l])
                bitwise_or = bits_to_dec()
                l += 1
        return shortest if shortest != math.inf else -1
            
