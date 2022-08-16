n = int(input())
l1 = [int(i) for i in input().split()]
max_sum = 0

for i in range(n):
    for j in range(i, n, 2):
        A = l1[i:j+2]
        A = sum(A[::2])
        for k in range(n):
            for l in range(k, n, 3):
                B = l1[k:l+3]
                B = sum(B[::3])
                if A == B and A >= max_sum:
                    max_sum = A
print(max_sum)
