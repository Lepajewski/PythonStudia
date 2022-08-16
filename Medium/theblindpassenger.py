tests = int(input())
seat_nums = []
results = []
for i in range(tests):
    seat_nums.append(input())
for i in seat_nums:
    if i == '1':
        results.append("poor conductor")
    else:
        RowNo = 0
        side = 'R'
        position = 'W'
        if i[-1] == '2' or i[-1] == '1':
            side = 'L'
        elif i[-1] == '3' or i[-1] == '0':
            position = 'A'
            side = 'L'
        if i[-1] == '4' or i[-1] == '9':
            position = 'A'
        elif i[-1] == '5' or i[-1] == '8':
            position = 'M'
        if i[-1] == '5' or i[-1] == '6' or i[-1] == '0' or i[-1] == '1':
            RowNo = int(i) // 5
        else:
            RowNo = int(i) // 5 + 1
        results.append([RowNo, position, side])
for i in results:
    if i == 'poor conductor':
        print(i, end='')
    else:
        for j in i:
            print(j, '', end='')
    print()
