N = int(input())
S = []
for _ in range(N):
    S.append(list(map(int, input().split())))
    
team_players = N // 2

team1 = [0]   # 첫번째 사람은 무조건 team 1에 배정
team2 = []

answer = float('inf')   # 정답 담기
    
# 새 사람이 팀에 배치됐을 때 추가되는 점수
def calc_score(team, new):
    result = 0
    for t in team:
        result += S[t][new]
        result += S[new][t]
    return result
        

# i번째 사람을 팀에 배치 (단 i는 0부터 시작)
def pick(i, score1, score2):
    global answer
    
    if len(team1) >= team_players and len(team2) >= team_players:
        answer = min(answer, abs(score1 - score2))    
    
    if len(team1) < team_players:
        add_score = calc_score(team1, i)
        team1.append(i)
        pick(i + 1, score1 + add_score, score2)
        team1.pop()
    if len(team2) < team_players:
        add_score = calc_score(team2, i)
        team2.append(i)
        pick(i + 1, score1, score2 + add_score)
        team2.pop()
    
pick(1, 0, 0)
print(answer)