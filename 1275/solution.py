from typing import List

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [[None]*3 for _ in range(3)]
        
        for i, (r, c) in enumerate(moves):
            board[r][c] = 'X' if i % 2 == 0 else 'O'
        
        # check rows, columns, diagonals in one pass
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != None:
                return 'A' if board[i][0] == 'X' else 'B'
            if board[0][i] == board[1][i] == board[2][i] != None:
                return 'A' if board[0][i] == 'X' else 'B'
        
        if board[0][0] == board[1][1] == board[2][2] != None:
            return 'A' if board[0][0] == 'X' else 'B'
        if board[0][2] == board[1][1] == board[2][0] != None:
            return 'A' if board[0][2] == 'X' else 'B'
        
        return 'Draw' if len(moves) == 9 else 'Pending'
