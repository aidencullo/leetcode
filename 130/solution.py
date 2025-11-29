class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def fill(r, c):
            def outside_grid(r, c):
                return r < 0 or r >= len(board) or c < 0 or c >= len(board[0])

            if (r, c) in seen:
                return True
            
            if outside_grid(r, c):
                return False

            if board[r][c] == 'X':
                return True

            seen.add((r, c))

            if (fill(r, c - 1)
                and fill(r, c + 1)
                and fill(r - 1, c)
                and fill(r + 1, c)):
                board[r][c] = 'X'
                return True
            return False
        
        seen = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                fill(i, j)                    
