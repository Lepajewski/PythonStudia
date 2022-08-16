input_list = input().split()

iterator = 0
s_of_given_numbers = 0

def s_up(s_in_func, i):
    x = int(input_list[i])
    s_in_func += x
    i += 1
    if i < len(input_list):
        s_up(s_in_func, i)
    elif i == len(input_list):
        print(s_in_func)
   
s_up(s_of_given_numbers, iterator)

