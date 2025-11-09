class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        prev = math.inf
        for num in nums:
            if num > prev:
                break
            prev = num
        else:
            return True
        prev = -math.inf
        for num in nums:
            if num < prev:
                break
            prev = num
        else:
            return True
        return False
