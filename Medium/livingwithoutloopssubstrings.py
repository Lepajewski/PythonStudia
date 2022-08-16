s = input()

def substring(start, length, string, res):
    
    if start + length <= len(string):
        print(string[start], string[start + length - 1])
        if string[start] == string[start + length - 1]:
            res += 1
        substring(start + 1, length, string, res)
    elif length + start + 1 > len(string) and length != len(string):
        substring(0, length + 1, string, res)
    else:
        print(res)
    
substring(0, 1, s, 0)
