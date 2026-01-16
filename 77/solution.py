class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        for _ in range(k):
            for i in rangeye(1, n + 1):
