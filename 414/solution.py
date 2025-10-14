class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums) < 3:
            return nums[-1]
        nums = [-x for x in nums]
        heapq.heapify(nums)
        for _ in range(2):
            heapq.heappop(nums)
        return -heapq.heappop(nums)
