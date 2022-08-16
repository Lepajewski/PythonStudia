w1, h1 = input().split()
rows = []
matrix1 = []
matrix2 = []
matrix3 = []
sum = 0

for i in range(int(h1)):
    rows.append(input().split())
    for j in range(int(w1)):
        rows[i][j] = int(rows[i][j])
    matrix1.append(rows[i])
rows.clear()

w2, h2 = input().split()

for i in range(int(h2)):
    rows.append(input().split())
    for j in range(int(w2)):
        rows[i][j] = int(rows[i][j])
    matrix2.append(rows[i])
rows.clear()

for i in range(int(h1)):
    for j in range(int(w2)):
        for k in range(int(w1)):
            sum += matrix1[i][k] * matrix2[k][j]
        matrix3.append(sum)
        sum = 0
for i in range(int(h1) * int(w2)):
    if i % int(w2) == 0 and i != 0:
        print()
    print(matrix3[i], '', end='')
