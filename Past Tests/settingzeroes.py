#m - kolumny
#n - wiersze
n, m = map(int, input().split())
matrix = []
x, y = [], []

for i in range(n):
    matrix.append([x for x in input().split()])
    
for i in range(n):
    for j in range(m):
        if matrix[i][j] == '0':
            x.append(i)
            y.append(j)
            
for i in range(len(x)):
    matrix[x[i]] = ['0' for i in range(m)]
    for j in range(n):
        matrix[j][y[i]] = '0'

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()
