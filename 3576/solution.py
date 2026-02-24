class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        def makeFlips(nums, target):
            flips = 0
            nums_copy = nums[:]

            for i in range(n - 1):
                if nums_copy[i] != target:
                    nums_copy[i] *= -1
                    nums_copy[i + 1] *= -1
                    flips += 1

            if nums_copy[-1] == target:
                return flips
            else:
                return math.inf
        
        flips = math.inf
        n = len(nums)
        flips = min(flips, makeFlips(nums, -1))
        flips = min(flips, makeFlips(nums, 1))
        return flips <= k
