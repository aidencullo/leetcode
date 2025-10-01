import numpy as np

class Solution:
    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
        current = np.array(mat)
        target = np.array(target)
        for _ in range(4):
            if np.array_equal(current, target):
                return True
            current = np.flip(current.T, axis=1)
        return False
