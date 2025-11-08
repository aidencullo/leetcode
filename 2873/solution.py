class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_triple = max_diff = max_val = 0
        for num in nums:
            max_triple = max(max_triple, max_diff * num)
            max_diff = max(max_diff, max_val - num)
            max_val = max(max_val, num)
        return max_triple
