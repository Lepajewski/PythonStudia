n = int(input())
mat = []
min_distance = 1000
distance = -1

for i in range(n):
    mat.append([int(j) for j in input().split()])

for i in range(n):
    for j in range(n):
        for k in range(n):
            for l in range(n):
                if i != k or j != l:
                    if mat[i][j] == 1 and mat[k][l] == 1:
                        if (k+1) / (i+1) == (k+1) // (i+1) and (l+1) / (j+1) == (l+1) // (j+1):
                            distance = abs((i+1) - (k+1)) + abs((j+1) - (l+1))
                        else:
                            distance = 1000
                        if distance < min_distance:
                            min_distance = distance
print(min_distance)

'''
for i in range(n):
    for j in range(n):
        i1, j1 = -1, -1
        i2, j2 = -1, -1
        for k in range(n):
            for l in range(n):
                if mat[k][l] == 1:
                    i1, j1 = k+1, l+1
                    print('xd',k,l)
                    break
        else: 
            break
        #print('1:', i1, j1)
        for k in range(i1-1, n):
            for l in range(j1-1, n):
                if mat[k][l] == 1:
                    i2, j2 = k+1, l+1
                    print('abc', k, l)
                    break
        else:
            break
        
        #print('2:', i2, j2)
'''
