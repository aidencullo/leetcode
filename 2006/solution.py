class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        res = 0
        for num in nums:
            res += seen[num + k]
            res += seen[num - k]
            seen[num] += 1
        return res
