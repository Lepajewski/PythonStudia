n = int(input())
students = {}
tests = {}
tests_number = {}

for i in range(n):
    inpt = input().split()
    name = inpt[0]
    marks = inpt[1::]
    sum_to_avg = 0
    for el in marks:
        score = float(el[el.index(':')+1::])
        sum_to_avg += score
        test_id = el[0:el.index(':')]
        if test_id in tests:
            tests[test_id] += score
            tests_number[test_id] += 1
        else:
            tests[test_id] = score
            tests_number[test_id] = 1
        
    students[name] = sum_to_avg / len(marks)
sorted(tests_number)

for i in sorted(students):
    print(i, students[i])
for i in sorted(tests):
    print(i, tests[i]/tests_number[i])
