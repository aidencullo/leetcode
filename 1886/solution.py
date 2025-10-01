class Solution:
    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
        def rotate(mat):
            return [list(row) for row in zip(*mat[::-1])]
            
        n = len(mat)
        current = mat
        for _ in range(4):
            if current == target:
                return True
            current = rotate(current)
        return False
