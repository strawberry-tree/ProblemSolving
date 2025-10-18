from collections import defaultdict

def solution(enroll, referral, seller, amount):    
    result = defaultdict(int)  # 각 구성원의 수입
    # {돈 내는사람 : 돈 받는 사람}
    referrer = dict({enroll[i]: referral[i] for i in range(len(enroll))})
    
    # 10%를 추천인에게 보내고 나머지는 내가 가짐
    def add_money(name, profit):
        bribe = int(profit * 0.1)
        result[name] += profit - bribe
        bribe_name = referrer[name]
        
        if bribe < 1 or bribe_name == "-":
            return
        add_money(bribe_name, bribe)
    
    for i in range(len(seller)):
        name = seller[i]       # 판매자
        profit = amount[i] * 100    # 발생 이익
        add_money(name, profit)
        
    answer = []
    
    for name in enroll:
        answer.append(result[name])
        
    return answer