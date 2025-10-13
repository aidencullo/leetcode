class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        value_keys = [(v, i) for i, v in enumerate(nums)]
        nsmall = heapq.nsmallest(value_keys)
        return nsmall
