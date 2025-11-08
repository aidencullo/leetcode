class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] == nums[j]:
                        continue
                    if nums[i] == nums[k]:
                        continue
                    if nums[j] == nums[k]:
                        continue
                    count += 1
        return count
