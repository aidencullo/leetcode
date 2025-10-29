class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        triplets = 0
        n = len(nums)
        seen = set()
        for k in range(n):
            if nums[k] - diff in seen and nums[k] - 2 * diff in seen:
                triplets += 1
            seen.add(nums[k])
        return triplets
