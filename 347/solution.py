from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)  # frequency map
        # heap of (frequency, num)
        heap = [(freq, num) for num, freq in count.items()]
        # get k largest by frequency
        return [num for freq, num in heapq.nlargest(k, heap)]
