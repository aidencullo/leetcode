class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        rows = len(board)
        cols = len(board[0])
        rook_r, rook_c = next((i, j) for i, row in enumerate(board) for j, x in enumerate(row) if x == 'R')
        pawns = 0
                    
        r, c = rook_r, rook_c
        while r < rows: 
            if board[r][c] == 'p':
                pawns += 1
                break
            if board[r][c] == 'B':
                break
            r += 1

        r, c = rook_r, rook_c
        while r >= 0:
            if board[r][c] == 'p':
                pawns += 1
                break
            if board[r][c] == 'B':
                break
            r -= 1

        r, c = rook_r, rook_c
        while c < cols:
            if board[r][c] == 'p':
                pawns += 1
                break
            if board[r][c] == 'B':
                break
            c += 1

        r, c = rook_r, rook_c
        while c >= 0:
            if board[r][c] == 'p':
                pawns += 1
                break
            if board[r][c] == 'B':
                break
            c -= 1


        return pawns
