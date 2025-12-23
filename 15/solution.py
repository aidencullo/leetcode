class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()
        n = len(nums)
        nums.sort()
        for i in range(n):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                if j != 0 and nums[j] == nums[j - 1]:
                    continue
                if -nums[i] - nums[j] in seen:
                    res.append([nums[i], nums[j], -nums[i] - nums[j]])
            seen.add(nums[i])
        return res
