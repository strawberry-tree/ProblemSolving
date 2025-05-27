# 인덱스 start부터 end까지 히스토그램의 최대넓이
def get_area(hist, start, end):
    
    # 종료조건 - 면적이 1일 때
    if start == end:
        return hist[start]
    
    mid = (start + end) // 2
    
    # 왼쪽 영역 최댓값
    left = get_area(hist, start, mid)
    
    # 오른쪽 영역 최댓값
    right = get_area(hist, mid + 1, end)
    
    # 왼쪽, 오른쪽을 가로지르는 영역 최댓값
    l = mid
    r = mid + 1
    
    cross = 0
    height = min(hist[l], hist[r])
    # 어케 풀지
    while True:
        area = (r - l + 1) * height
        cross = max(area, cross)
        
        if l <= start and end <= r:
            break
        elif l <= start:    # j를 우측으로 이동
            height = min(height, hist[r + 1])
            r += 1
        elif end <= r:      # i를 좌측으로 이동
            height = min(height, hist[l - 1])
            l -= 1
        else:
            r_height = min(height, hist[r + 1])
            l_height = min(height, hist[l - 1])
            if l_height > r_height:
                height = l_height
                l -= 1
            else:
                height = r_height
                r += 1

    return max(left, right, cross)

while True:
    num_input = input()
    if num_input == "0":
        break
    hist = list(map(int, num_input.split()))[1:]
    print(get_area(hist, 0, len(hist) - 1))