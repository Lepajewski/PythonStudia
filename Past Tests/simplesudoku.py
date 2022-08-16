sudoku = []
res = -1
numbers = '123456789'
#i - wiersze, j - kolumny
for i in range(9):
    sudoku.append(input().split())
    
for i in range(9):
    col = [sudoku[j][i] for j in range(9)]
    for j in range(9):
        if sudoku[i].count(numbers[j]) > 1 or col.count(numbers[j]) > 1:
            res = False
            break
if res == False:
    print(res)
else:
    res = 'X'
    diagA = []
    diagB = []
    for i in range(9):
        diagA.append(sudoku[i][i])
        diagB.append(sudoku[i][8-i])

    for i in range(9):
        #print(diagA[i], numbers[i], diagA.count(numbers[i]))
        #print(diagB[i], numbers[i], diagB.count(numbers[i]))
        if diagA.count(numbers[i]) > 1 or diagB.count(numbers[i]) > 1:
            res = True
    print(res)
