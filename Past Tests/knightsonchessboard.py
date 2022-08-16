n = int(input())
board = []
attacks = 0

for i in range(n+2):
    if i == 0 or i==n+1:
        board.append('a' * (n+4))
        board.append('a' * (n+4))
    else:
        board.append('aa' + input() + 'aa')

for i in range(2, n+2):
    for j in range(2, n+2):
        if board[i][j] == 's':
            if board[i-2][j-1] == 's':
                attacks += 1
            if board[i-2][j+1] == 's':
                attacks += 1
            if board[i-1][j-2] == 's':
                attacks += 1
            if board[i-1][j+2] == 's':
                attacks += 1
            if board[i+1][j-2] == 's':
                attacks += 1
            if board[i+1][j+2] == 's':
                attacks += 1
            if board[i+2][j-1] == 's':
                attacks += 1
            if board[i+2][j+1] == 's':
                attacks += 1
print(attacks)
