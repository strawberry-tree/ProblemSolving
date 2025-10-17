from collections import defaultdict
def solution(genres, plays):
    # 장르별 재생횟수
    genre_plays = defaultdict(int)
    
    for i in range(len(genres)):
        genre_plays[genres[i]] += plays[i]
        
    # 제일 많이 재생된 두 장르
    sorted_genres = sorted(list(genre_plays.keys()), reverse=True, key=lambda g: genre_plays[g])
    
    # 2개씩 빼기
    answer = []
    for tg in sorted_genres:
        tg_plays = [(i, plays[i]) for i in range(len(genres)) if genres[i] == tg]
        tg_plays.sort(key=lambda x:x[1], reverse=True)
        for i in range(min(len(tg_plays), 2)):
            answer.append(tg_plays[i][0])
    
    return answer