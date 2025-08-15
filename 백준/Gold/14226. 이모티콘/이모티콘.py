from collections import deque

# (화면 이모티콘 개수, 클립보드 이모티콘 개수, 몇초?)
S = int(input())
queue = deque([(1, 0, 0)])
visited = set() # (화면 이모티콘 개수, 클립보드 이모티콘 개수) 기록

while queue:
    screen, clip, sec = queue.popleft()
    
    if screen == S:
        print(sec)
        break
    
    # 이때 클립보드는 덮어 씌우기 처리한다.
    if (screen, screen) not in visited:
        # 1. 화면에 있는 모든 이모티콘을 모두 복사해서 클립보드에 저장한다.
        visited.add((screen, screen))
        queue.append((screen, screen, sec + 1))

    if clip > 0 and (screen + clip, clip) not in visited:    
        # 2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
        visited.add((screen + clip, clip))
        queue.append((screen + clip, clip, sec + 1))
    
    
    if screen > 0 and (screen - 1, clip) not in visited:
        # 3. 화면에 있는 이모티콘 중 하나를 삭제한다.
        visited.add((screen - 1, clip))
        queue.append((screen - 1, clip, sec + 1))