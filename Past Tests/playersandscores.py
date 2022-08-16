n = int(input())

players = {}
players_wins = {}

for i in range(n):
    p1, p2 = input().split()
    p1_id = p1[:p1.index(':')]
    p1_score = int(p1[p1.index(':') + 1::])
    p2_id = p2[:p2.index(':')]
    p2_score = int(p2[p2.index(':') + 1::])
    
    if p1_score > p2_score:
        if p1_id in players:
            players[p1_id] += p1_score
        else:
            players[p1_id] = p1_score
        if p2_id in players:
            players[p2_id] += p2_score
        else:
            players[p2_id] = p2_score
        players_wins[p1_id] += 1
        players_wins[p2_id] += 0
    elif p1_score < p2_score:
        if p1_id in players:
            players[p1_id] += p1_score
        else:
            players[p1_id] = p1_score
        if p2_id in players:
            players[p2_id] += p2_score
        else:
            players[p2_id] = p2_score
        players_wins[p2_id] += 1
        players_wins[p1_id] += 0
        
print(players)
print(players_wins)
players_wins = sorted(players_wins.items(), key = lambda a: (-a[1], -players[a[0]], a[0]))

for i in players_wins():
    print(i[0])
