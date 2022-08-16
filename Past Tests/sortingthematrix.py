#m - kolumny
#n - wiersze
n, m = map(int, input().split())
matA = []
matB = []

for i in range(n):
    matA.append([int(x) for x in input().split()])
for i in range(n):
    for j in range(m):
        matB.append(matA[i][j])
matB.sort()
'''for i in range(n*m):
    if i % m == 0 and i > 0:
        print() 
    print(matB[i], end= ' ')'''
#print()
for i in range(n):
    for j in range(m):
        print(matB[i + j*n], end = ' ')
    print()
