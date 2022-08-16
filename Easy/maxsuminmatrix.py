dimension = int(input())
matrix = []
sums = []

for i in range(dimension):
    matrix.append([int(x) for x in input().split()])

for wiersz in range(dimension):
    sum_temp = 0
    for j in range(dimension):
        for k in range(j, dimension):
            sum_temp += matrix[wiersz][k]
        sums.append(sum_temp)
        sum_temp = 0

print(sums)
