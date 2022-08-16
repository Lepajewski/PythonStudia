n = int(input())
results = []

for i in range(n):
    
    value, type1, type2 = input().split()
    value = float(value)
    if type1 == "Celsius" and type2 == "Kelvin":
        if value < -273.15:
            results.append('NO')
        else:
            results.append('{0:.2f}'.format(round(value + 273.15, 2)))
    if type1 == "Celsius" and type2 == "Fahrenheit":
        if value < -273.15:
            results.append('NO')
        else:
            results.append('{0:.2f}'.format(round((value * 9.0/5.0) + 32.0, 2)))
    if type1 == "Kelvin" and type2 == "Celsius":
        if value < 0.0:
            results.append('NO')
        else:
            results.append('{0:.2f}'.format(round(value - 273.15, 2)))
    if type1 == "Kelvin" and type2 == "Fahrenheit":
        if value < 0.0:
            results.append('NO')
        else:
            results.append('{0:.2f}'.format(round((value * 9.0/5.0) - 459.67, 2)))
    if type1 == "Fahrenheit" and type2 == "Celsius":
        if value < -459.67:
            results.append('NO')
        else:
            results.append('{0:.2f}'.format(round((value - 32.0) / (9.0/5.0), 2)))
    if type1 == "Fahrenheit" and type2 == "Kelvin":
        if value < -459.57:
            results.append('NO')
        else:
            results.append('{0:.2f}'.format(round((value + 459.67) * (5.0 / 9.0), 2)))
            
for i in range(n):
    print(results[i])
