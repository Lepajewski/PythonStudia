#n - wiersze
#m - kolumny
rows, columns = map(int, input().split())
word = input()
matrix = [input() for i in range(rows)]

for i in range(rows):
    print(matrix[i], matrix[i][::-1])
    if word in matrix[i] or word in matrix[i][::-1]:
        print('YES')
        break
else:
    for i in range(columns):
        col = ''.join(matrix[j][i] for j in range(rows))
        print(col, col[::-1])
        if word in col or word in col[::-1]:
            print('YES')
            break
    else:
        print('NO')
