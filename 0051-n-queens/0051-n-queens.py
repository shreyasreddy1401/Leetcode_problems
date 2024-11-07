class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for i in range(n)]
        ans = []
        
        def safe(board, row, col, n):
            # Check the upper-left diagonal
            r, c = row, col
            while r >= 0 and c >= 0:
                if board[r][c] == 'Q':
                    return False
                r -= 1
                c -= 1
            
            # Check the left side (same row)
            c = col
            while c >= 0:
                if board[row][c] == 'Q':
                    return False
                c -= 1
            
            # Check the lower-left diagonal
            r, c = row, col
            while r < n and c >= 0:
                if board[r][c] == 'Q':
                    return False
                r += 1
                c -= 1
                
            return True
        
        def solve(board, col, ans, n):
            if col == n:
                solution = [''.join(row) for row in board]  # Convert the board to the correct output format
                ans.append(solution)
                return
                
            for row in range(n):
                if safe(board, row, col, n):
                    board[row][col] = 'Q'
                    solve(board, col + 1, ans, n)
                    board[row][col] = '.'
        
        solve(board, 0, ans, n)
        return ans
