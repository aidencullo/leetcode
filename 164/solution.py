from typing import List

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        min_val = min(nums)
        max_val = max(nums)

        bucket_size = ceil((max_val - min_val) / (n-1))

        bucket_count = (max_val - min_val) // bucket_size + 1

        maxs = [None] * bucket_count
        mins = [None] * bucket_count

        for num in nums:
            bucket = num // bucket_size
            maxs[bucket] = max(num, maxs[bucket]) if max[bucket] else num
            mins[bucket] = min(num, mins[bucket]) if min[bucket] else num

        prev = None
        for i in range(bucket_count):
            if not maxs[i]:
                continue
            max_gap = max(max_gap, mins[i] - prev) if prev else 0
            prev = maxs[i]

        return max_gap
