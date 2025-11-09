class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        if r * c != rows * cols:
            return mat
        data = []
        for row in range(rows):
            for col in range(cols):
                data.append(mat[row][col])
        data_index = 0
        reshaped = [[0] * c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                reshaped[i][j] = data[data_index]
                data_index += 1
        return reshaped
