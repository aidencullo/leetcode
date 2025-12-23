class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()
        n = len(nums)
        nums.sort()
        for i in range(n):
            for j in range(i + 1, n):
                if -nums[i] - nums[j] in seen:
                    res.append([nums[i], nums[j], -nums[i] - nums[j]])
            seen.add(nums[i])
        return [list(t) for t in set(tuple(triplet) for triplet in res)]
