from collections import deque
n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x,y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        # 현재 위치에서 상하좌우 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 그래프 범위르 벗어나는 경우 -> x
            if nx <0 or nx >=n or ny <0 or ny >=m:
                continue
            
            # 새 위치가 벽인 경우 -> x
            if graph[nx][ny] == 0:
                continue

            # 노드를 처음 방문 => 해당 그래프에 최단거리를 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    
    return graph[n-1][m-1]

print(bfs(0, 0))
            