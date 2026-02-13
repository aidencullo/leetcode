class Solution:
    def findKDistantIndices(self, nums, key, k):
        key_positions = [i for i, v in enumerate(nums) if v == key]

        key_idx = 0
        res = []

        for i, num in enumerate(nums):
            while key_idx < len(key_positions) and key_positions[key_idx] + k < i:
                key_idx += 1
            if abs(key_positions[key_idx] - i) <= k:
                res.append[i]

        return res
