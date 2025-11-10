class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return [list(items) for items in zip(*matrix)]
