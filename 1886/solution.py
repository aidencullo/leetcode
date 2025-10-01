import numpy as np

class Solution:
    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
        current = np.array(mat)
        target = np.array(target)
        for _ in range(4):
            if np.array_equal(mat, target)  # True
                return True
            current = np.rot90(current)
        return False
