class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        low = min(nums)
        high = max(nums)
        all_nums = dict.fromkeys(range(low, high + 1))
        for num in nums:
            all_nums.pop(num)
        return list(all_nums.keys())
