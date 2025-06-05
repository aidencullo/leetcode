import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = []
        self.k = k
        for num in nums:
            heapq.heappush(self.nums, num)
            if len(self.nums) > self.k:
                heapq.heappop(self.nums)
                

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
