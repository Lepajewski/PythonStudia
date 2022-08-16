brackets = input()
opening = '([{'
closing = ')]}'
flag = True

if brackets[0] == closing[0] or brackets[0] == closing[1] or brackets[0] == closing[2] or brackets[-1] == opening[0] or brackets[-1] == opening[1] or brackets[-1] == opening[2]:
    flag = False
elif len(brackets) % 2 != 0:
    flag = False
else:
    op, cl = 0, 0
    for j in range(3):
        for i in range(len(brackets)):
            if brackets[i] == closing[j]:
                cl += 1
            if brackets[i] == opening[j]:
                op += 1
        if op != cl:
            flag = False
        op, cl = 0, 0
    else:
        for i in range(len(brackets)-1, 1, -1):
            for j in range(3):
                if brackets[i] == closing[j] and brackets[i-1] != opening[j] and brackets[i-1] != closing[0] and brackets[i-1] != closing[1] and brackets[i-1] != closing[2]:
                    flag = False
        if len(brackets) == 2:
            for j in range(3):
                if brackets[1] == closing[j] and brackets[0] != opening[j]:
                    flag = False        
print(flag)
