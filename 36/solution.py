class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_unique(arr):
            arr = [x for x in arr if x]
            return len(set(arr)) == len(arr)

        def has_max_nine(arr):
            return max(arr) <= 9

        def has_min_one(arr):
            return min(arr) >= 1
        
        def contains_one_through_nine(arr):
            return is_unique(arr) and has_max_nine(arr) and has_min_one(arr)

        def get_submats(mat):
            import numpy as np
            narr = np.array(mat)
            for i in range(3):
                for j in range(3):
                    yield narr[i * 3: i * 3 + 3, j * 3: j * 3 + 3]

        if not all(contains_one_through_nine(row) for row in board):
            return False

        # if not all(contains_one_through_nine(col) for col in zip(*board)):
        #     return False

        # if not all(contains_one_through_nine(mat) for mat in mat_to_list(get_submats(board))):
        #     return False

        return True
        
