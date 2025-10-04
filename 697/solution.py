from collections import Counter

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        nums_counter = Counter(nums)
        nums_degree = max(nums_counter.values())

        degree = 0
        counter = Counter()
        i = 0
        j = 0
        import math
        shortest_subarray = math.inf
        n = len(nums)
        total = 0
        while i < n:
            while degree < nums_degree and i < n:
                counter[nums[i]] += 1
                degree = max(counter[nums[i]], degree)
                i += 1
                total += 1
            while degree == nums_degree:
                if degree == counter[nums[j]]:
                    degree -= 1
                counter[nums[j]] -= 1
                j += 1
                total -= 1
            shortest_subarray = min(shortest_subarray, total + 1)
        return shortest_subarray
        
