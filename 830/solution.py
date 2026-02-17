from itertools import groupby

class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        data = s
        current = 0
        res = []
        for k, group in groupby(data):
            lst = list(group)
            if len(lst) >= 3:
                res.append([current, current + len(lst) - 1])
            current += len(lst)
        return res

