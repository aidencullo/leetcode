class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])

        if r * c != rows * cols:
            return mat

        data = []
        reshaped = [[0] * c for _ in range(r)]

        for row in range(rows):
            for col in range(cols):
                data_index = row * cols + col
                new_row = data_index // c
                new_col = data_index % c
                reshaped[new_row][new_col] = mat[row][col]
        return reshaped
