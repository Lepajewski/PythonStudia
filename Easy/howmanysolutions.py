n, x, y = map(int, input().split())
solutions = 0

for a in range(n+1):
    for b in range(n+1):
        for c in range(n+1):
            for d in range(n+1):
                print(a,b,c,d)
                if x*a*a + y*b*b == x*c*c + y*d*d:
                    solutions += 1
print(solutions)
