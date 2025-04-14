def givemoney(money, me, total, pyramid):
    # 선형트리인 경우 최대 N단계 올라감
    donate = int(money * 0.1)
    rest = money - donate
    total[me] += rest
    if donate > 0 and pyramid[me] != "-":
        givemoney(donate, pyramid[me], total, pyramid)
    
def solution(enroll, referral, seller, amount):
    # key 자식 판매원, value 부모 판매원
    pyramid = {enroll[i]: referral[i] for i in range(len(enroll))}
    pyramid["-"] = None
    
    # key 판매원, value 정산 금액
    total = {e: 0 for e in enroll}
    
    # 정산
    for i in range(len(seller)):
        givemoney(amount[i] * 100, seller[i], total, pyramid)
    
    # result 배열 만들기
    result = []
    for e in enroll:
        result.append(total[e])
    return result