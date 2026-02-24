class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        flips = math.inf
        n = len(nums)

        target = 1
        target_flips = 0
        nums_copy = nums[:]

        for i in range(n - 1):
            if nums_copy[i] != target:
                nums_copy[i] *= -1
                nums_copy[i + 1] *= -1
                target_flips += 1

        if nums_copy[-1] == target:
            flips = min(flips, target_flips)


        target = -1
        target_flips = 0
        nums_copy = nums[:]

        for i in range(n - 1):
            if nums_copy[i] != target:
                nums_copy[i] *= -1
                nums_copy[i + 1] *= -1
                target_flips += 1

        if nums_copy[-1] == target:
            flips = min(flips, target_flips)

        return flips <= k
