n = int(input())
max_area = 0
min_area = 0
points = []

#points[x][y]

    
for i in range(n):
    x, y = input().split()
    points.append([int(x), int(y)])

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            #print("Xa=", points[i][0], "Ya=", points[i][1])
            #print("Xb=", points[j][0], "Yb=", points[j][1]) 
            #print("Xc=", points[k][0], "Yc=", points[k][1]) 
            area = 0.5 * abs((points[j][0] - points[i][0])*(points[k][1] - points[i][1]) - (points[j][1] - points[i][1]) * (points[k][0] - points[i][0]))
            #print(i, j, k, area)
            if area >= max_area:
                max_area = area
            if area <= min_area:
                min_area = area

print(max_area, min_area)
