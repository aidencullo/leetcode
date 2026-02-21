class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        def transform(mat, r, c):
            new_mat = [row[:] for row in mat]

            for j in range(len(mat[0])):
                new_mat[r][j] += 1

            for i in range(len(mat)):
                new_mat[i][c] += 1

            return new_mat

        
        mat = [[0] * m for i in range(n)]
        for r, c in indices:
            mat = transform(mat, r, c)


        res = 0
        for row in mat:
            for el in row:
                if el % 2 == 1:
                    res += 1
        return res
