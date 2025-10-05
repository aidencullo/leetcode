class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        all_nums = set(range(1, n + 1))
        for x in nums:
            all_nums.discard(x)
        return list(all_nums)
