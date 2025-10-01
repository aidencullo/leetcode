def rotate(mat):
    n = len(mat)
    return [
        [mat[-(j + 1)][i] for j in range(n)]
        for i in range(n)
    ]

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        current = mat

        for _ in range(4):
            current = rotate(current)
            if current == target:
                return True
        return False
