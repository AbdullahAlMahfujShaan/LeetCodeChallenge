class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        def is_valid(board, row, col, num):
            # Check row
            for x in range(9):
                if board[row][x] == num:
                    return False

            # Check column
            for x in range(9):
                if board[x][col] == num:
                    return False

            # Check 3x3 box
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == num:
                        return False

            return True
        
        def solve(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for num in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                            if is_valid(board, i, j, num):
                                board[i][j] = num
                                if solve(board):
                                    return True
                                board[i][j] = '.' # backtrack
                        return False
            return True # Solution found
        
        solve(board)
