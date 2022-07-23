from collections import deque

def solution(maps):
    answer = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append((0, 0))
    graph = [[-1 for _ in range(5)] for _ in range(5)]
    graph[0][0] = 1
    
    while q:
        x, y = q.popleft()
        # 상하좌우로 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 안에 들고 그 칸이 벽이 아닐 경우 queue에 추가
            if 0<=nx<5 and 0<=ny<5 and maps[nx][ny]==1:
                if graph[nx][ny] == -1:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))
    return graph[4][4]