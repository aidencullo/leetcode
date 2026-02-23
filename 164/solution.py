class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(set(nums)) < 2:
            return 0
        
        min_val = min(nums)
        max_val = max(nums)
        n = len(nums)

        bucket_size = ceil((max_val - min_val) / (n-1))
        bucket_count = (max_val - min_val) // bucket_size + 1

        maxs = [None] * bucket_count
        mins = [None] * bucket_count

        for num in nums:
            bucket = (num - min_val) // bucket_size
            if maxs[bucket] is None:
                maxs[bucket] = mins[bucket] = num
            else:
                maxs[bucket] = max(num, maxs[bucket])
                mins[bucket] = min(num, mins[bucket])

        prev = min_val
        max_gap = 0
        for i in range(bucket_count):
            if maxs[i] is None:
                continue
            max_gap = max(max_gap, mins[i] - prev)
            prev = maxs[i]

        return max_gap
