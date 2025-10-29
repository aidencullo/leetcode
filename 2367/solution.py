class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        seen = set()
        triplets = 0
        for num in nums:
            if num - diff in seen and num - 2 * diff in seen:
                triplets += 1
            seen.add(num)
        return triplets
