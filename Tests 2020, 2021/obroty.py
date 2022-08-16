import copy
n, m = map(int, input().split())
mat_X = []
mat_Y = []
res = 'NIE'
end = False
for i in range(n):
    mat_X.append([int(i) for i in input().split()])
for i in range(n):
    mat_Y.append([int(i) for i in input().split()])

if mat_X == mat_Y:
    res = 'TAK'
else:
    for i in range(n):
        for j in range(m):
            mat = copy.deepcopy(mat_X)
            for k in range(n):
                mat.append(mat_X[k])
            mat[i] = mat[i][j:] + mat[i][:j]
            if mat[i] == mat_Y[i]:
                res = 'TAK'
                end = True
                break
        else:
            break
    if res == 'NIE':
        for i in range(m):
            for j in range(n):
                mat = copy.deepcopy(mat_X)
                col = []
                for k in range(n):
                    col.append(mat_X[k][i])
                col = col[j:] + col[:j]
                for k in range(n):
                    mat[k][i] = col[k]
                if mat == mat_Y:
                    res = 'TAK'
                    break
            else:
                break
print(res)
