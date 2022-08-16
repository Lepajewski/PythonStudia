board = ['aaaaaaaaaa']
k_x, k_y = 0, 0

for i in range(8):
    board.append('a' + input() + 'a')
    for j in range(10):
        if board[i][j] == 'k':
            k_x, k_y = i, j
board.append('aaaaaaaaaa')

def verdict():
    for i in range(k_x-1, k_x+2):
        for j in range(k_y-1, k_y+2):
            if board[i][j] == 'a':
                continue
            if i == k_x and j == k_y:
                if 'w' not in board[k_x][:k_y] + board[k_x][k_y+1:]:
                    if 'w' not in [board[k][k_y] for k in range(10)]:
                        return 'pat'
            if 'w' not in board[i][:j] + board[i][j+1:]:
                if 'w' not in [board[k][j] for k in range(10) if k != i]:
                    return 'game goes on'
    return 'mat'

print(verdict())
    



'''
for i in range(k_x-1, k_x+2):
    for j in range(k_y-1, k_y+2):
        if board[i][j] == 'a':
            continue
        elif j = k_y and i = k_x:
            if (board[i][:j] + board[i][j+1:]).find('w') == False:
                f = True
                for k in range(10):
                    if board[k][k_y] == 'w':
                        f = False
                if f == True:
                    res = 'pat'
        if (board[i][:j] + board[i][j+1:]).find('w') == False:
            f = True
            for k in range(10):
                if k == i:
                    continue
                if board[k][k_y] == 'w':
                    f = False
           if f == True:
               res = 'game goes on'

print(res)


for i in range(k_x-1, k_x+2):
    col = ''
    for j in range(10):
        if board[j][i] != 'a' and j != k_y-1 and j != k_y and j != k_y+1:
            col += board[j][i]
    if 'w' in col:
        n_col += 1
    print(col)
print(n_col)
for i in range(k_y-1, k_y+2):
    row = ''
    for j in range(10):
        if board[i][j] != 'a' and j != k_x-1 and j != k_x and j != k_x+1:
            row += board[i][j]
    print(row)
    if 'w' in row:
        n_row += 1
print(n_row)

for i in range(k_y-1, k_y+2):
    for j in range(k_x-1, k_x+2):
        if board[i][j] == 'w':
            neighbours += 1
print(neighbours)
'''
    
    
    
    
    
    
    
    
    
    
    
    
