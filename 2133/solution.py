class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        def unique(mat):
            return all(len(set(row)) == len(row) for row in mat)

        def less_than(arr):
            return np.all(arr <= len(arr))

        def valid(mat):
            return less_than(mat) and unique(mat)

        import numpy as np

        arr = np.array(matrix)
        
        return valid(arr) and valid(arr.T)
