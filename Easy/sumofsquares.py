a, b = input().split()
a = int(a)
b = int(b)
sum_a = 0
sum_b = 0

def power(arg):
    return arg**2

for i in range(b - a + 1):
    sum_a += power(a + i)
    
print(sum_a)
