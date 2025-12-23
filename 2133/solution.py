class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        def valid(mat):
            return all(set(row) == oneToN for row in mat)
        
        oneToN = set(range(1, len(matrix) + 1))
        return valid(matrix) and valid(zip(*matrix))
