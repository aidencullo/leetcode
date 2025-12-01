class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def dfs(r, c):

            if not (0 <= r < len(board) and 0 <= c < len(board[0])):
                return

            if (r, c) in seen:
                return

            seen.add((r, c))

            if board[r][c] == 'X':
                return

            if board[r][c] == 'O':
                board[r][c] = '-'

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)


        seen = set()
                
        row = 0
        for col in range(len(board[0])):
            dfs(row, col)

        row = len(board) - 1
        for col in range(len(board[0])):
            dfs(row, col)
                
        col = 0
        for row in range(len(board)):
            dfs(row, col)

        col = len(board[0]) - 1
        for row in range(len(board)):
            dfs(row, col)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '-':
                    board[i][j] = 'O'
                   
