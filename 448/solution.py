class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        all_nums = set(range(1, len(nums) + 1))
        given_nums = set(nums)
        diff = all_nums - given_nums
        return list(diff)
