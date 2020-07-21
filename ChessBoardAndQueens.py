count = 0
board = [[0 for i in range(8)]for i in range(8)]
row = [False for i in range(8)]
diag1 = [False for i in range(15)]
diag2 = [False for i in range(15)]
for i in range(8):
    s = input()
    for j in range(8):
        board[i][j] = 1 if s[j] == '*' else 0
def solve(board,col, count):
    res = False
    if col == 8:
        return True,count+1
    for i in range(8):
        if board[i][col] != 1 and row[i] == False and diag1[i+col]==False and diag2[col-i+7] == False:
            board[i][col] = 1
            row[i] = True
            diag1[i+col] = True
            diag2[col-i+7] = True
            useful,count = solve(board, col+1, count)
            res = res or useful
            board[i][col] = 0
            row[i] = False
            diag1[i+col] = False
            diag2[col-i+7] = False
    return res,count

print(solve(board,0,count)[1])