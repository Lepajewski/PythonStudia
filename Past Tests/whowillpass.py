n = int(input())
matrix = []
results = []

for i in range(n+2):
    if i == 0 or i == n+1:
        matrix.append(['x' for j in range(n+2)])
    else:
        matrix.append(['x'] + [int(j) for j in input().split()] + ['x'])
        results.append([0 for j in range(n)])

for i in range(1, n+1):
    for j in range(1, n+1):
        if matrix[i][j] >= 3:
            results[i-1][j-1] = 1
        else:
            avg = 0
            neighbours = 0
            
            if matrix[i-1][j-1] != 'x':
                avg += matrix[i-1][j-1]
                neighbours += 1
            if matrix[i-1][j] != 'x':
                avg += matrix[i-1][j]
                neighbours += 1
            if matrix[i-1][j+1] != 'x':
                avg += matrix[i-1][j+1]
                neighbours += 1
            if matrix[i][j+1] != 'x':
                avg += matrix[i][j+1]
                neighbours += 1
            if matrix[i][j-1] != 'x':
                avg += matrix[i][j-1]
                neighbours += 1
            if matrix[i+1][j-1] != 'x':
                avg += matrix[i+1][j-1]
                neighbours += 1
            if matrix[i+1][j] != 'x':
                avg += matrix[i+1][j]
                neighbours += 1
            if matrix[i+1][j+1] != 'x':
                avg += matrix[i+1][j+1]
                neighbours += 1
            
            avg = avg / neighbours
            if avg >= 3:
                results[i-1][j-1] = 1
            #print(matrix[i][j], avg*neighbours, avg, neighbours, results[i-1][j-1])

for i in range(n):
    for j in range(n):
        print(results[i][j], end=' ')
    print()
