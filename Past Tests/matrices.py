n = int(input())
matA = []
matB = []
done = False

for i in range(n):
    matA.append(input().split())
for i in range(n-1):
    matB.append(input().split())
    
for i in range(n):
    mat1 = matA[:i] + matA[i+1::]

    for j in range(n):
        mat2 = []
        for k in range(n-1):
            mat2.append(mat1[k][:j] + mat1[k][j+1::])
        
        if mat2 == matB:
            print('True')
            done = True
            break
if done == False:
    print('False')
