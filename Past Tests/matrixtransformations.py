#m - wiersze | n - kolumny
m, n = map(int, input().split())
mat = []

for i in range(m):
    mat.append([int(i) for i in input().split()])
    
k = int(input())

for i in range(k):
    operation = input()
    if operation == 'T':
        matB = []
        m, n = n, m
        for j in range(m):
            column = []
            for k in range(n):
                column.append(mat[k][j])
            matB.append(column)
        print(matB)
        mat = matB
        print(mat)
    elif operation[1] == 'R':
        row = int(operation[operation.index(" "):])
        mat[row] = mat[row][::-1]
    else:
        col = int(operation[operation.index(" "):])
        column = []
        for j in range(m):
            column.append(mat[j][col])
        column = column[::-1]
        for j in range(m):
            mat[j][col] = column[j]
        
for i in range(m):
    for j in range(n):
        print(mat[i][j], end=' ')
    print()
