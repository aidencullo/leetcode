from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def valid_mat(submat):
            seq = [x for row in submat for x in row]
            nums = list(filter(str.isdigit, seq))
            return len(set(nums)) == len(nums)

        def valid_seq(seq):
            nums = list(filter(str.isdigit, seq))
            return len(set(nums)) == len(nums)

        for row in board:
            if not valid_seq(row):
                return False

        cols = [list(col) for col in zip(*board)]
        for col in cols:
            if not valid_seq(col):
                return False

        for i in range(3):
            for j in range(3):
                submatrix = [row[j * 3: j * 3 + 3] for row in board[i * 3: i * 3 + 3]]
                if not valid_mat(submatrix):
                    return False
            
        
        return True
