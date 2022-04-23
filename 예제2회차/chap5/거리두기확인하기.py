from collections import deque
        
def bfs(place, d):  # 거리두기가 지켜졌으면 True, 안지켜졌으면 False를 출력
    q = deque()
    visited = [[False]*5 for _ in range(5)]
    q.append(d)   # d:[행, 열, 거리]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while q:
        x, y, dist = q.popleft()
        visited[x][y] = True
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            ndist = dist + 1
            
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                visited[nx][ny] = True  # 방문처리
                
                if place[nx][ny] == 'P': # 거리 2 이내에 응시자가 있으면 -> 거리두기 실패
                    if ndist <= 2:
                        return False
                elif place[nx][ny] == 'O': # 빈 공간인데 거리가 1이면 한칸 더 가볼 수 있음 -> q에 저장
                    if ndist == 1:
                        q.append([nx, ny, ndist])
    return True

def solution(places):
    answer = []
    for place in places:  # 모든 위치의 응시자 확인
        result = 1
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    if not bfs(place, [i, j, 0]):  # 한번이라도 False가 뜨면 0
                        result = 0
        answer.append(result)
    
    return answer