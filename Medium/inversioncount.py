n = int(input())
A = []
inversion = 0

for i in range(n):
    A.append(int(input()))
    
for i in range(n-1):
    for j in range(i, n):
        if A[i] > A[j]:
            inversion += 1
print(inversion)
