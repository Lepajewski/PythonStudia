a = int(input())
dic_names = {}
dic_grades = {}
dic_count = {}

for i in range(a):
    n = input().split()
    dic_names[n[0]] = 0
    for x in n[1:]:
        k = x[:x.find(':')]
        v = float(x[x.find(':') + 1:])
        dic_names[n[0]] += v
        if k in dic_grades:
            dic_count[k] += 1
            dic_grades[k] += v
        else:
            dic_count[k] = 1
            dic_grades[k] = v
    dic_names[n[0]] /= (len(n) - 1)

for i in sorted(dic_names.keys()):
    print(i, dic_names[i])

for i in sorted(dic_grades.keys()):
    print(i, dic_grades[i] / dic_count[i])
