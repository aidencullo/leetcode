class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        def check_square(r, c, l):
            if r + l >= len(matrix):
                return False

            if c + l >= len(matrix[0]):
                return False

            return all(matrix[r][c] == 1 for r, c in zip(range(r, r + l), range(c, c + l)))

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                i = 1
                while True:
                    if not check_square(row, col, i):
                        break

                    max_sq = max(max_sq, i ** 2)
                    i += 1
        
        max_sq = 0
        return max_sq

            
