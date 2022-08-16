h, w, x, y = map(int, input().split())
wall = []
res = False

for i in range(h):
    wall.append([int(j) for j in input().split()])

for i in range(h):
    if i <= h-x:
        for j in range(w):
            if wall[i][j] == 0:
                zeros = 0
                a = 0
                while j+a < w:
                    if wall[i][j+a] == 0:
                        zeros += 1
                    a += 1
                if zeros >= y:
                    n_col = 0
                    for k in range(y):
                        col = []
                        for l in range(x):
                            col.append(wall[i+l][j+k])
                        if sum(col) == 0:
                            n_col += 1
                        else:
                            break
                    if n_col >= y:
                        res = True
print(res)
            
