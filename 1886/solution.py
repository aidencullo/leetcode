import copy

def rotate(mat):
    new_mat = copy.deepcopy(mat)
    n = len(mat)
    for i in range(n):
        for j in range(n):
            new_mat[i][j] = mat[-(j + 1)][i]
    return new_mat

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        current = mat

        for _ in range(4):
            current = rotate(current)
            if current == target:
                return True
        return False
