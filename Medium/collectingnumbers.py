dimension = int(input())
matrix = []
path_sum = 0

for i in range(dimension):
    matrix.append([int(x) for x in input().split()])
    
i, j = 0, 0 #wiersz, kolumna

while i < dimension and j < dimension:
    path_sum += matrix[i][j]
    if i < dimension - 1 and j < dimension - 1:
        if matrix[i + 1][j] > matrix[i][j + 1]:
            path_sum += matrix[i + 1][j]
            i += 1
        else:
            path_sum += matrix[i][j + 1]
            j += 1
    elif i == dimension - 1:
        path_sum += matrix[i][j + 1]
        j += 1
    elif j == dimension - 1:
        path_sum += matrix[i + 1][j]
        i += 1
        
print(path_sum)
