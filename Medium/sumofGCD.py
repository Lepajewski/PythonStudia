tests = int(input())
number_lists = []
results = []

def gcd(a, b):
    while b != 0:
        c = b
        b = a % b
        a = c
    return a

for i in range(tests):
    number_lists.append(list(map(int, input().split())))
    sum_gcd = 0
    for j in range(1, len(number_lists[i])):
        for k in range(j + 1, len(number_lists[i])):
            sum_gcd += gcd(number_lists[i][j], number_lists[i][k])
    results.append(sum_gcd)

for i in results:
    print(i)
