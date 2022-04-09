from collections import deque
        
def bfs(place, d):
    q = deque()
    visited = [[False]*5 for _ in range(5)]
    q.append(d)
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
                visited[nx][ny] = True
                
                if place[nx][ny] == 'P':
                    if ndist <= 2:
                        return False
                elif place[nx][ny] == 'O':
                    if ndist == 1:
                        q.append([nx, ny, ndist])
    return True

def solution(places):
    answer = []
    for place in places:
        result = 1
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    if not bfs(place, [i, j, 0]):
                        result = 0
        answer.append(result)
    
    return answer