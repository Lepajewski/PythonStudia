n = int(input())
l1 = []
instruments = []
for i in range(n):
    tmp = input().split()
    l1.append(tmp)

for i in range(n):
    for j in range(i+1, n):
        for k in [0, 1, 2]:
            for l in [0, 1, 2]:   
                #print(l1[i][:k] + l1[i][k+1:], l1[i][k])
                #print(l1[j][:l] , l1[j][l+1:], l1[j][l])
                l2 = l1[i][:k] + l1[i][k+1:]
                l3 = l1[j][:l] + l1[j][l+1:]
                if l2 == l3 or l2 == l3[::-1]:
                    #print(l1[i][:k] + l1[i][k+1:], 'a', l1[j][:l] + l1[j][l+1:])
                    if l1[i][k] not in instruments:
                        instruments.append(l1[i][k])
                    if l1[j][l] not in instruments:
                        instruments.append(l1[j][l])
for i in sorted(instruments):
    print(i)
