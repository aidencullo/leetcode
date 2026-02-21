from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

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
            
        
        return True
