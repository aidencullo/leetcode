class Solution:
    def findKDistantIndices(self, nums, key, k):
        distant_indices = set()
        
        for i, num in enumerate(nums):
            if num == key:
                distant_indices.update(range(i - k, i + k + 1))


        valid_distant_indices = {idx for idx in distant_indices if 0 <= idx < len(nums)}
        return sorted(valid_distant_indices)
