class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])

        if r * c != rows * cols:
            return mat

        from itertools import chain
        from itertools import batched
        data = list(chain.from_iterable(mat))
        reshaped = list(batched(data, c))
        return reshaped
