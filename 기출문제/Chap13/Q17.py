from collections import deque
N, K = map(int, input().split())

graph = []   # 보드 정보 
data = []  #바이러스 정보

for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(N):  
        # 해당 위치에 바이러스가 존재할경우 data에 넣기
        if graph[i][j] != 0:
            #(바이러스 종류, 시간, 위치 X, 위치 Y)
            data.append((graph[i][j], 0, i, j))


# 데이터 정렬(낮은 번호가 먼저 증식함)
data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

# 바이러스가 퍼져나갈 수 있는 위치
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# bfs
while q:
    virus, s, x, y = q.popleft()
    if s == target_s:
        break

    # 현재 노드에서 위치 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 해당 위치로 이동할 수 있는 경우
        if 0 <= nx and nx < N and 0 <= ny and ny <N :
            # 아직 방문 x -> 바이러스 넣기
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s+1, nx, ny))

print(graph[target_x - 1][target_y - 1])  # 0부터 시작했으니까 1 빼주기