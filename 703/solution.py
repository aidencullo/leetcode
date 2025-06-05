class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = []
        self.k = k
        for num in nums:
            bisect.insort(self.nums, num)
            if len(self.nums) > self.k:
                self.nums.pop(0)

    def add(self, val: int) -> int:
        bisect.insort(self.nums, val)
        if len(self.nums) > self.k:
            self.nums.pop(0)
        return self.nums[0]
       


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
