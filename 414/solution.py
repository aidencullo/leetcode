class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        max_three = heapq.nlargest(3, nums)
        return max_three[2] if len(max_three) == 3 else max_three[0]
