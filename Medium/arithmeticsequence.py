n, k = input().split()
n = int(n)
k = int(k)
add = False

def sequence(a, b, flag):
    if a > b - k and flag == False:
        a -= b
        if a <= 0:
            flag = True
        print(a, end=' ')
        sequence(a, b, flag)
    elif a < n:
        a += b
        print(a, end=' ')
        sequence(a, b, flag)
       
print(n, end=' ')    
sequence(n, k, add)
