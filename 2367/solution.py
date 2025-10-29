class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        triplets = 0
        n = len(nums)
        seen = set()
        for j in range(n):
            for k in range(j + 1, n):
                if nums[k] - nums[j] == diff and nums[j] - diff in seen:
                    triplets += 1
            seen.add(nums[j])
        return triplets
