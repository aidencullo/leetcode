from typing import List
from collections import defaultdict

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        res = defaultdict(int)

        for k, v in items1 + items2:
            res[k] += v

        return sorted(res.items())
