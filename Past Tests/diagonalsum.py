#n, m - wiersze, kolumny
n, m = map(int, input().split())
matrix = []
max_diagonal = 0

for i in range(n):
    matrix.append([int(i) for i in input().split()])

if n > m:
    for i in range(n):
        matrix[i] += [0] * (n-m)
    m = n
if n < m:
    for i in range(m-n):
        matrix.append([0] * m)
    n = m

for i in range(n):
    diagonal_sum = 0
    for j in range(n-i):
        diagonal_sum += matrix[i+j][j]
        print(i, j, matrix[i+j][j])
    if diagonal_sum > max_diagonal:
        max_diagonal = diagonal_sum
    print(diagonal_sum)
    diagonal_sum = 0
    for j in range(n-1-i):
        diagonal_sum += matrix[j][i+j+1]
    if diagonal_sum > max_diagonal:
        max_diagonal = diagonal_sum
    diagonal_sum = 0
    for j in range(n-i, 0, -1):
        diagonal_sum += matrix[n-j-i][j-1]
    if diagonal_sum > max_diagonal:
        max_diagonal = diagonal_sum
    diagonal_sum = 0
    for j in range(n-1-i):
        diagonal_sum += matrix[n-j-1][j+i+1]
    if diagonal_sum > max_diagonal:
        max_diagonal = diagonal_sum
        
print('a', max_diagonal)



































































