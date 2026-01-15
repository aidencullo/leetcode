class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for k, v in counter.items():
            if v == len(nums) // 2:
                return k
