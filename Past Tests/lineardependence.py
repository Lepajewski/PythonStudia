n = int(input())
mat = []
vectors = 0

for i in range(n):
    mat.append([int(j) for j in input().split()])
  
for i in range(n):
    for j in range(i+1, n):
        row1 = mat[i]
        row2 = mat[j]
        dependent = True
        if all(k for k in row1) == 0 or all(k for k in row2) == 0:
            dependent = False
        if row2[0] != 0:
            r = row1[0] / row2[0]
        for k in range(1, n):
            if row2[k] != 0:
                if row1[k] / row2[k] != r:
                    dependent = False
                    break
            else:
                dependent = False
                break
        if dependent == True:
            print(row1, row2)
            vectors += 1
        col1 = []
        col2 = []
        for k in range(n):
            col1.append(mat[k][i])
            col2.append(mat[k][j])
        dependent = True
        if all(k for k in col1) == 0 or all(k for k in col2) == 0:
            dependent = False
        if col2[0] != 0:
            r = col1[0] / col2[0]
        for k in range(1, n):
            if col2[k] != 0 and col1[k] != 0:
                if col1[k] / col2[k] != r:
                    dependent = False
            elif col2[k] == 0 and col2[k] == 0:
                dependent = True
            else:
                dependent = False
                break
        if dependent == True:
            print(col1, col2)
            vectors += 1
for i in range(n):
    row = mat[i]
    for j in range(n):
        col = []
        for k in range(n):
            col1.append(mat[k][j])
        dependent = True
        if all(k for k in row) == 0 or all(k for k in col) == 0:
            dependent = False
        if col[0] != 0:
            r = row[0] / col[0]
        for k in range(1, n):
            if row[k] != 0 and col[k] != 0:
                if row[k] / col[k] != r:
                    dependent = False
            elif row[k] == 0 and col[k] == 0:
                dependent = True
            else:
                dependent = False
                break
        if dependent == True:
            #print(col1, col2)
            vectors += 1
print(vectors)            
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
'''
for i in range(n-1):
    for j in range(i+1, n):
        flag = False
        row1 = mat[i]
        row2 = mat[j]
        if row2[0] != 0:
            r = row1[0] / row2[0]
            for k in range(1,n):
                if row2[k] != 0:
                    if row1[k]/row2[k] == r:
                        flag = True
                elif row2[k] == 0 and row1[k] == 0:
                    flag = True
            if flag == True:
                vectors += 1
        flag = False
        col1, col2 = [], []
        for k in range(n):
            col1.append(mat[k][i])
            col2.append(mat[k][j])
        if col2[0] != 0:
            r = col1[0] / col2[0]
            for k in range(1,n):
                if col2[k] != 0:
                    if col1[k]/col2[k] == r: 
                        flag = True
                    elif col2[k] == 0 and col1[k] == 0:
                        flag = True
            if flag == True:
                vectors += 1
print(vectors)'''
