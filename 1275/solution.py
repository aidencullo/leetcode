from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:

        def check_diag(board):
            if all(board[i][i] == 'X' for i in range(3)):
                return True

            if all(board[i][i] == 'O' for i in range(3)):
                return True

            if all(board[2 - i][i] == 'X' for i in range(3)):
                return True

            if all(board[2 - i][i] == 'O' for i in range(3)):
                return True


        def check_rows(board):
            if any(all(el == 'X' for el in row) for row in board):
                return True

            if any(all(el == 'O' for el in row) for row in board):
                return True

        def transpose(matrix):
            return [list(col) for col in zip(*matrix)]

        def winner(board):
            if check_rows(board):
                return True

            cols_as_rows = transpose(board)
            if check_rows(cols_as_rows):
                return True

            if check_diag(board):
                return True

            return False

        def get_winner():
            return 'A' if len(moves) % 2 == 1 else 'B'

        def complete():
            return len(moves) == 9
            
        board = [[None] * 3 for i in range(3)]

        for i, (r, c) in enumerate(moves):
            board[r][c] = 'X' if i % 2 == 0 else 'O'

        if winner(board):
            return get_winner()

        if not winner(board) and not complete():
            return 'Pending'
        else:
            return 'Draw'
            
