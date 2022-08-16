l = input().split()

for i in range(len(l)):
    l[i] = int(l[i])
l.sort()

start = l[0]
stop = l[-1] + 1
result = -1
step = 1
l1 = list((range(1, stop + 1)))

while result == -1:
    l2 = list(range(start, stop, step))
    if l2 == l:
        result = True
        break
    elif step < stop:
        step += 1
    else:
        result = False
print(result)
