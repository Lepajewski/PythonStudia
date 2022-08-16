import math
n = int(input())
mat = [[int(x) for x in input().split()] for i in range(n)]
steps = math.ceil(n / 2)
x = 0
for i in range(steps):
    for j in range(x, n-x):
        print(mat[x][j], end=' ')
    for j in range(x+1, n-x):
        print(mat[j][n-1-x], end=' ')
    for j in range(n-1-x, x, -1):
        print(mat[n-1-x][j-x-1], end=' ')
    for j in range(n-2-x, x, -1):
        print(mat[j][x], end=' ')
    x += 1



