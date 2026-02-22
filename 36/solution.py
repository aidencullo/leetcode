from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if not val.isdigit():
                    continue

                box = (r // 3) * 3 + (c // 3)

                if val in cols[c]:
                    return False

                if val in rows[r]:
                    return False

                if val in boxes[box]:
                    return False

                cols[c].add(val)
                rows[r].add(val)
                boxes[box].add(val)


        return True
