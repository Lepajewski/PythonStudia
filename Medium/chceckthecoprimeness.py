tests = int(input())
results = []


def gcd(a, b):
    while b != 0:
        c = b
        b = a % b
        a = c
    return a

def is_one(c, d):
    for i in range(d, 0, -1):
        if gcd(c, i) == 1:
            return i

for i in range(tests):
    n = int(input())
    results.append(is_one(n, n // 2))

for i in results:
    print(i)
