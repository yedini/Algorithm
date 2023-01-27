from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    graph = [[-1]*m for _ in range(n)]
    q = deque()
    q.append((0, 0))
    graph[0][0] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and maps[nx][ny] == 1 and graph[nx][ny] == -1:
                q.append((nx, ny))
                graph[nx][ny] = graph[x][y]+1
                
    return graph[-1][-1]