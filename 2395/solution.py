class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        seen = set()
        n = len(nums)
        for i in range(n - 1):
            pairSum = nums[i] + nums[i + 1]
            if pairSum in seen:
                return True
            seen.add(pairSum)
        return False
