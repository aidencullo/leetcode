from typing import List


class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        def process_bottom_left_triangle():
            n = len(grid)
            for starting_row in range(n):
                seq = []
                col = 0
                for row in range(starting_row, n):
                    seq.append(grid[row][col])
                    col += 1
                seq_sorted = sorted(seq, reverse=True)
                col = 0
                for row in range(starting_row, n):
                    grid[row][col] = seq_sorted[col]
                    col += 1

        def process_top_right_triangle():
            n = len(grid)
            for starting_col in range(1, n):
                seq = []
                row = 0
                for col in range(starting_col, n):
                    seq.append(grid[row][col])
                    row += 1
                seq_sorted = sorted(seq)
                row = 0
                for col in range(starting_col, n):
                    grid[row][col] = seq_sorted[row]
                    row += 1

        process_bottom_left_triangle()
        process_top_right_triangle()

        return grid
