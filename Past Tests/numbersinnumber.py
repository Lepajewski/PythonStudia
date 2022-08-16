n = input()

for i in range(len(n)):
    most_fq = 0
    nmb = 0
    for j in range(len(n) - i):
        tmp = n[j:j+i+1]
        kant = 0
        for k in range(len(n) - i):
            substring = n[k:k+i+1]
            if tmp == substring:
                kant += 1
        if kant > most_fq:
            nmb = int(tmp)
            most_fq = kant
        elif kant == most_fq:
            if nmb > int(tmp):
                nmb = int(tmp)
                most_fq = kant
    print(nmb)
