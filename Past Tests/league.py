n, m, t = map(int, input().split())
teams_wins = {}
teams_played = {}

for i in range(n):
    team = input()
    teams_wins[team] = 0
    teams_played[team] = 0

for i in range(m):
    match = input().split(':')
    teams_played[match[0]] += 1
    teams_played[match[1]] += 1
    if int(match[2]) > int(match[3]):
        teams_wins[match[0]] += 1
    else:
        teams_wins[match[1]] += 1
print(teams_played)
print(teams_wins)
for i in sorted(teams_wins.items(), key = lambda x: x[0]):
    #print(n-1-teams_played[i] + teams_wins[i])
    if n-1-teams_played[i[0]] + i[1] >= t:
        print(i[0])
