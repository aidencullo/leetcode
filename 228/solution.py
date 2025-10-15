class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        def format_range(l, r):
            if l < r:
                return "{}->{}".format(l, r)
            return "{}".format(r)

        if not nums:
            return []

        ranges = []
        last = nums[0]
        start = nums[0]
        n = len(nums)
        for i in range(1, n):
            x = nums[i]
            if x != last + 1:
                ranges.append([start, last])
                start = x
            last = x
            
        ranges.append([start, last])

        ranges = [format_range(start, end) for start, end in ranges]

        return ranges
