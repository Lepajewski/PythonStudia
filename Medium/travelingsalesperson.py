n = int(input())
cities = []
coordinates = []
length = 0
city = 0
next_city = 0

for i in range(n):
    string = list(input().split())
    cities.append(string[0])
    coordinates.append((int(string[1]), int(string[2])))
trip_order = list(input().split())

for i in range(n-1): #x2 - x1 y2 - y1
    #[[poznan, 0, 0], [warszawa, 0, 5], [krakow, 5, 5], [gdansk, 5, 0]]
    #poznan = cities[0][0]
    city = coordinates[cities.index(trip_order[i])] #(x, y)
    next_city = coordinates[cities.index(trip_order[i+1])]
    
    length += ((next_city[0] - city[0])**2 + (next_city[1] - city[1])**2)**0.5
beg = coordinates[cities.index(trip_order[0])]
last = coordinates[cities.index(trip_order[-1])]
length += ((beg[0] - last[0])**2 + (beg[1] - last[1])**2)**0.5
print(length)
