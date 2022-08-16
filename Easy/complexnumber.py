import math

complex_number = input()
i = 0
Re = ''
Im = ''

while complex_number[i] != ' ':
    Re += complex_number[i]
    i += 1
i = len(complex_number) - 2
while complex_number[i] != ' ':
    Im += complex_number[i]
    i -= 1
Re = float(Re)
Im = float(Im[::-1])

modulus = (Re**2 + Im**2)**(0.5)
if modulus == math.trunc(modulus):
    modulus = math.trunc(modulus)
    
if Im == 0.0 and Re == 0.0:
    print(modulus)
    print(0)
elif Re > 0:
    argument = math.atan(Im/Re)
    print(modulus)
    print(argument)
elif Re < 0:
    argument = math.atan(Im/Re) + math.pi
    print(modulus)
    print(argument)
else:
    print(modulus)
    if Im > 0:
        print(math.pi / 2.0)
    else:
        print(round(2.0/3.0 * math.pi, 3))
