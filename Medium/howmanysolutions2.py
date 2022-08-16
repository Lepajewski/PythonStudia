n, x, y = map(int, input().split())
solutions = 0

for a in range(n+1):
    for b in range(n+1):
        for c in range(n+1):
            for d in range(n+1):
                if x*a*a + y*b*b == x*c*c + y*d*d:
                    solutions += 1
                    print(a, b, c, d, 'a')
                else:
                    print(a, b, c, d)
print(solutions)

solutions = 0
for a in range(n+1):
    for b in range(n+1):
        for c in range(n+1):
            for d in range(n+1):
                if (a==c and b==d) or (a==d and b==c):
                    solutions += 1
                    print(a,b,c,d,'a')
print(solutions)
'''
solutions = 0
for a in range((n+1)**4):
    b =
'''   
