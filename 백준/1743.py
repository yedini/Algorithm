# bfs 이용
from collections import deque
n, m, k = map(int, input().split())
graph = [[0]*(m+1) for _ in range(n+1)]   # 맵 생성

for _ in range(k):
    tx, ty = map(int, input().split())
    graph[tx][ty] = 1  # 음식물은 1로 표시

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(i, j, graph):
    q = deque([[i, j]])
    graph[i][j] = 2   # 한번 방문한 음식물은 2로 표시
    result = 1

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 < nx <= n and 0 < ny <= m and graph[nx][ny] == 1:
                q.append([nx, ny])
                graph[nx][ny] = 2
                result += 1
    return result   # [i,j] 위치랑 같이 묶인 음식물 개수 출력

answer = 0

for i in range(1, n+1):
    for j in range(1, m+1):
        if graph[i][j] == 1:   # [i,j] 위치가 음식물일 경우 주변 확인
            ans = bfs(i, j, graph)
            answer = max(ans, answer)

print(answer)