No = int(input())

def a(n, dic):
    if n in dic: return dic[n]
    tmp = 1 + a(n + 1 - a(a(n, dic), dic), dic)
    dic[n] = tmp
    return tmp
print(a(No, {0:1})
      
def a(n):
    if n == 1:
        return 1
    else:
        n -= 1
        return 1 + a(n + 1 - a(a(n)))

    
    
def Fib_2(n, d):
    if n in d: return d[n]
    tmp = Fib_2(n-1), d) + Fib_2(n-2, d)
    d[n] = tmp
    return tmp

Fib_2(10, {0:1, 1:1})
    '''if n == len(results):
        return results[n - 1]
    else:
        n -= 1
        print('n', n)
        return 1 + a(n + 1 - a(results[n - 1]))'''

'''for i in range(1, No, 1):
    results.append(a(i + 1))'''

print(a(No))
