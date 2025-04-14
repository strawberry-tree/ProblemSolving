def solution(phone_book):
    # O(N log N)
    phone_book.sort(key = lambda x: len(x))
    phone_set = set()
    
    # phone_book의 길이가 N일 때 (O(N))
    for number in phone_book:
        # 전화번호의 길이는 최대 20
        for i in range(len(number)):
            if number[:i+1] in phone_set:
                return False
        phone_set.add(number)
    return True