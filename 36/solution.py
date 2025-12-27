class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def has_nine_unique_els(arr):
            return len(set(arr)) == 9

        def has_max_nine(arr):
            return max(arr) == 9

        def has_min_one(arr):
            return max(arr) == 1
        
        def contains_one_through_nine(arr):
            return has_nine_unique_els(arr) and has_max_nine(arr) and has_min_one(arr)

        if not all(contains_one_through_nine(row) for row in board):
            return False

        if not all(contains_one_through_nine(col) for col in zip(*board)):
            return False

        if not all(contains_one_through_nine(mat) for mat in mat_to_list(get_mats(board))):
            return False

        return True
        
