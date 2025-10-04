class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        def degree(lst):
            if not lst:
                return
            counter = Counter(lst)
            return counter.most_common(1)[0][1]

        def generate_subarrays(lst):
            subarrays = []
            n = len(lst)
            for start in range(n):
                for end in range(start, n):
                    subarrays.append(lst[start: end + 1])
            return subarrays
            
        
        nums_degree = degree(nums)
        subarrays = generate_subarrays(nums)
        import math
        smallest_possible_length = math.inf
        for subarray in subarrays:
            if degree(subarray) == nums_degree:
                smallest_possible_length = min(smallest_possible_length, len(subarray))
        return smallest_possible_length
