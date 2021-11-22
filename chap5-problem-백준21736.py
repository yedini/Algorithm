from collections import deque
N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(input()))

# starting point
for i in range(N):
    for j in range(M):
        if graph[i][j] == "I":
            graph[i][j] = "O"
            x = i
            y = j
            break

# 이동 방향(상 하 좌 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]



def bfs(x,y):
    count = 0
    queue = deque()
    queue.append((x,y))
    visited = [[True]*M for _ in range(N)]
    while queue:
        x,y = queue.popleft()

        # 현재 위치에서 네 방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 벗어날 경우 무시
            if nx >= N or nx <= -1 or ny >=M or ny<= -1:
                continue

            # 해당 노드를 처음 방문 & 벽이 아닌 경우
            elif graph[nx][ny] != 'X' and visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = False

                if graph[nx][ny] == "P":
                    count += 1
    return(count)


result = bfs(x,y)
if result == 0:
    result = "TT"
print(result)