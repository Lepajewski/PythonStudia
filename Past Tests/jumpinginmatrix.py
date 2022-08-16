n = int(input())
#a-wiersz, b-kolumna
a, b = map(int, input().split())
mat = []
f_row = f_col = True

for i in range(n):
    mat.append(list(map(int, input().split())))

if n == 1:
    print(a, b)
else:
    while True:
        row = mat[a]
        if mat[a][b] == min(row):
            col = []
            for j in range(n):
                col.append(mat[j][b])
            
            if mat[a][b] == min(col):
                break
            else:
                min_col = -1   
                for j in range(n):
                    if j == 0:
                        min_col = j
                    elif col[min_col] > col[j]:
                        min_col = j
                a = min_col
        else:
            min_row = -1
            for i in range(n):
                if i == 0:
                    min_row = i
                elif row[min_row] > row[i]:
                    min_row = i
            b = min_row

    print(a, b)
