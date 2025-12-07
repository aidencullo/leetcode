class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        low = min(nums)
        high = max(nums)
        all_nums = set(range(low, high + 1))
        for num in nums:
            all_nums.remove(num)
        return sorted(all_nums)
