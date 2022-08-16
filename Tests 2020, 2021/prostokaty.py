import copy
n = int(input())
res = 'NIE'
mat_x = [[int(j) for j in input().split()] for i in range(n)]
mat_y = [[int(j) for j in input().split()] for i in range(n)]

for i in range(n): #x_start
    for j in range(n): #y_start
        for k in range(n): #x_end
            for l in range(n): #y_end
                mat = copy.deepcopy(mat_x)
                
                if i == k and j == l:
                    if mat[i][j] == 1:
                        mat[i][j] = 0
                    else:
                        mat[i][j] = 1
                else:
                    rectangle = []
                    for m in range(min(i, k), abs(i-k) + min(i, k) + 1):
                        for o in range(min(j, l), abs(j-l) + min(j, l) + 1):
                            rectangle.append(mat[m][o])
                            if mat[m][o] == 1:
                                mat[m][o] = 0
                            else:
                                mat[m][o] = 1
                    print(i, j, k, l, rectangle)
                if mat == mat_y:
                    res = 'TAK'
                    print('xd')
                    break
            else:
                break
        else:
            break
    else:
        break
print(res)
