class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique_nums = list(set(nums))
        heapq.heapify(unique_nums)
        three_max = heapq.nlargest(3, unique_nums)
        return three_max[2] if len(three_max) == 3 else three_max[0]
