class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr_sorted = sorted(set(arr))
        rank = dict()
        for i, x in enumerate(arr_sorted):
            rank[x] = i + 1
        return [rank[x] for x in arr]
