from typing import List


class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        d1 = dict(items1)
        d2 = dict(items2)

        res = defaultdict(int)

        for k, v in d2.items():
            res[k] += v

        for k, v in d1.items():
            res[k] += v

        return sorted(list(item) for item in res.items())

