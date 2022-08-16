#m - kolumny
#n - wiersze
m, n = map(int, input().split())
matA = []
col = []
for i in range(n):
    matA.append([int(x) for x in input().split()])
for i in range(m):
    col.append(list(matA[j][i] for j in range(n)))
    col[i].sort()
for i in range(n):
    for j in range(m):
        print(col[j][i], end=' ')
    print()
