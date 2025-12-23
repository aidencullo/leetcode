class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        def valid(mat):
            return any(set(row) != one_to_n for row in mat)

        one_to_n = set(range(1, len(matrix) + 1))
        return valid(matrix) and valid(zip(*matrix))
