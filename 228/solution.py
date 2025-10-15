class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        def format_range(l, r):
            if l < r:
                return "{}->{}".format(l, r)
            return "{}".format(r)

        if not nums:
            return []

        ranges = []
        last = math.inf
        start = math.inf
        for i, x in enumerate(nums):
            if x != last + 1:
                ranges.append([start, last])
                start = x
            last = x
            
        ranges.append([start, last])

        ranges = ranges[1:]

        ranges = [format_range(start, end) for start, end in ranges]

        return ranges
