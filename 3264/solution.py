class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(v, i) for i, v in enumerate(nums)]
        heapq.heapify(heap)
        for _ in range(k):
            min_el, min_index = heapq.heappop(heap)
            nums[min_index] *= multiplier
            heapq.heappush(heap, (min_el * multiplier, min_index))
        return nums
