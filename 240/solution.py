class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        next_diagnol = bisect.bisect_left(range(min(rows, cols)), target, key=lambda i: matrix[i][i])
        if next_diagnol < min(rows, cols) and target in matrix[next_diagnol]:
            return True
        transpose_matrix = [list(col) for col in zip(*matrix)]
        if next_diagnol < min(rows, cols) and target in transpose_matrix[next_diagnol]:
            return True
        if next_diagnol > 0 and target in transpose_matrix[next_diagnol - 1]:
            return True
        if next_diagnol > 0 and target in matrix[next_diagnol - 1]:
            return True
        return False
