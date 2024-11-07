class Solution:
    def totalNQueens(self, n: int) -> int:
        count = 0
        board = [["."]*n for i in range(n)]
        def safe(board,row,col,n):
            r,c = row,col
            #upper-left diagonal
            while(r >= 0 and c >= 0):
                if board[r][c] == "Q":
                    return False
                r -= 1
                c -= 1
            c = col

            #left row
            while(c >= 0):
                if board[row][c] == "Q":
                    return False
                c -= 1
            
            #bottom-left diagonal
            r,c = row , col
            while(r < n and c >= 0):
                if board[r][c] == "Q":
                    return False
                c -= 1
                r += 1
            return True
        def solve(board,col,n):
            if col == n:
                return 1
            c = 0
            for row in range(n):
                if safe(board,row,col,n):
                    board[row][col] = "Q"
                    c += solve(board,col+1,n)
                    board[row][col] = "."
            return c
        return solve(board,0,n)
