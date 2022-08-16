n = int(input())
bottles = {}

for i in range(n):      #    0  1  2
    l = input().split() #id, S, W, V
    bottles[l[0]] = [float(x) for x in l[1::]]
operations = int(input())
for i in range(operations):
    A, B = input().split()
    free_space = bottles[B][2] - (bottles[B][0] + bottles[B][1])
    how_much = bottles[A][1] + bottles[A][0]
    if how_much > 0:
        if free_space >= how_much:
            bottles[B][0] += bottles[A][0]
            bottles[B][1] += bottles[A][1]
            bottles[A][0] = 0
            bottles[A][1] = 0
        else:
            juice = bottles[A][0] / how_much * free_space
            water = bottles[A][1] / how_much * free_space
            bottles[B][0] += juice
            bottles[B][1] += water
            bottles[A][0] -= juice
            bottles[A][1] -= water
    else:
        continue
        
for i in sorted(bottles.items()):
    print(i[1][0])


n = int(input())
b = {}
for i in range(n):
    x = input().split()
    s = int(x[1])
    w = int(x[2])
    v = int(x[3])
    b[x[0]] = [s, w, v]
m = int(input())
for i in range(m):
    p = input().split()
    skad = p[0]
    dakad = p[1]
    ile = b[skad][0] + b[skad][1]
    ilezmiesci = b[dakad][2] - b[dakad][1] - b[dakad][0]
    if ile <= ilezmiesci:
        b[dakad][0] += b[skad][0]
        b[dakad][1] += b[skad][1]
        b[skad][0] = 0
        b[skad][1] = 0
    elif ile > ilezmiesci:
        if ile > 0:
            sok = b[skad][0]/ile * ilezmiesci
            woda = b[skad][1]/ile * ilezmiesci
            b[skad][0] -= sok
            b[skad][1] -= woda
            b[dakad][0] += sok
            b[dakad][1] += woda
for key in sorted(b):
    print(b[key][0])


