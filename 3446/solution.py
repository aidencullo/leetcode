class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        def process_bottom_left_triangle():
            n = len(grid)
            for row_index in range(n):
                seq = [grid[j][j] for j in range(row_index, n)]
                seq_sorted = sorted(seq, reverse=True)
                for j in range(row_index, n):
                    grid[j][j] = seq_sorted[j - row_index]

        process_bottom_left_triangle()

        def process_top_right_triangle():
            n = len(grid)
            for col_index in range(1, n):
                seq = [grid[j][j] for j in range(col_index, n)]
                seq_sorted = sorted(seq, reverse=True)
                for j in range(row_index, n):
                    grid[j][j] = seq_sorted[j - row_index]

        process_top_right_triangle()

        return grid
