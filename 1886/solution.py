class Solution:
    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
        def rotate(row, col, rotations):
            for _ in range(rotations):
                row, col = col, -(row + 1)
            return row, col

        n = len(mat)
        for rotation in range(4):
            is_equal = True
            for row in range(n):
                for col in range(n):
                    rotated_row, rotated_col = rotate(row, col, rotation)
                    if target[row][col] != mat[rotated_row][rotated_col]:
                        is_equal = False
            if is_equal:
                return True
        return False
