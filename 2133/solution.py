class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        def unique(mat):
            return all(len(set(row)) == len(row) for row in mat)

        def less_than(arr):
            return np.all(arr <= len(mat))

        def valid(mat):
            return and_compose([unique, less_than], mat)

        def and_compose(iters, x):
            return reduce(lambda acc, f: acc and f(x), iters, True)


        import numpy as np

        arr = np.array(matrix)  # mat is your double list
        
        return valid(arr) and valid(arr.T)
