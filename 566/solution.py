class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])

        if r * c != rows * cols:
            return mat

        data = [item for row in mat for item in row]
        reshaped = []

        for i in range(0, len(data), c):
            reshaped.append(data[i: i + c])

        return reshaped
