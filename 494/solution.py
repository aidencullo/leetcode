class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        n = len(nums)
        sums = defaultdict(int)
        sums[0] = 1
        for num in nums:
            new_sums = defaultdict(int)
            for value, frequency in sums.items():
                new_sums[value + num] += frequency
                new_sums[value - num] += frequency
            sums = new_sums
        return sums[target]
