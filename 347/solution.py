from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        d = dict(counter)
        return [k for k, v in sorted(d.items(), key=lambda x: x[1])[-k:]]
