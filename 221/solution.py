class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        def calc_square(r, c, l):
            if r + l >= len(matrix):
                return 0

            if c + l >= len(matrix[0]):
                return 0
