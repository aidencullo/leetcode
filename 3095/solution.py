import math


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:

        def subtract_bits(x):
            for i in range(32):
                shield = 1 << i
                if shield & x:
                    bit_count[i] -= 1

        def add_bits(x):
            for i in range(32):
                shield = 1 << i
                if shield & x:
                    bit_count[i] += 1

        def bits_to_dec():
            dec = 0
            for i in range(32):
                bit = 1 << i
                dec += bit * (1 if bit_count[i] else 0)
            return dec

        bit_count = [0] * 32
        shortest = math.inf
        bitwise_or = 0
        l = 0
        n = len(nums)
        for i, x in enumerate(nums):
            add_bits(x)
            bitwise_or = bits_to_dec()
            while bitwise_or >= k and l <= i:
                shortest = min(shortest, i - l + 1)
                subtract_bits(nums[l])
                bitwise_or = bits_to_dec()
                l += 1
        return shortest if shortest != 0 and shortest != math.inf else -1
