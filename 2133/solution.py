class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        
        return all(len(set(row)) == len(row) for row in matrix) and all(max(row) <= len(row) for row in matrix) and all(len(set(col)) == len(col) for col in zip(*matrix)) and all(max(col) <= len(col) for col in zip(*matrix))
