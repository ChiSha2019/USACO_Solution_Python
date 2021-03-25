def isSafe(board, row: int, col: int) -> bool:
   if col == 0:
       return True

   #Check this row on left side
   for i in range(col):
       if board[row][i] == 1:
           return False

   #Check upper diagonal on left side
   if row > 0:
       i = row - 1
       j = col - 1
       while i >= 0 and j >= 0:
           if board[i][j] == 1:
               return False
           i -= 1
           j -= 1
   if row < len(board) - 1:
       i = row + 1
       j = col - 1
       while i < len(board) and j >= 0:
           if board[i][j] == 1:
               return False
           i += 1
           j -= 1
   return True

def printBoard(board):
   for row in board:
       print(row)
   print("---------")


def solveNQ(board, col):
    for row in range(len(board)):
        if row > 0:
            board[row-1][col] = 0
        board[row][col] = 1
        if isSafe(board, row, col) and col == len(board[row])-1:
            printBoard(board)
            return
        elif isSafe(board, row, col):
            solveNQ(board, col + 1)
        else:
            board[row][col] = 0

booard = [[0,0,0,0,],[0,0,0,0,],[0,0,0,0,],[0,0,0,0,]]
solveNQ(booard,0)