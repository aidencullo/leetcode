class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        import math
        longest = 0
        l, r = 0, 0
        n = len(nums)
        while r < n:
            while l < n and nums[l] % 2 and nums[l] < threshold:
                l += 1
            r = l
            while r < n and nums[r] <= threshold:
                if l != r:
                    if nums[r] % 2 == nums[r - 1] % 2:
                        l += 1
                        break
                r += 1
                longest = max(longest, r - l)
        return longest
        
            
                
