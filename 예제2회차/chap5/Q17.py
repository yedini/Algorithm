from collections import deque

n, k = map(int, input().split())
graph = []
virus = []  # 바이러스 정보
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        # 바이러스가 존재할 경우 virus에 종류, 시간, 위치를 저장
        if graph[i][j] != 0:
            virus.append((graph[i][j], 0, i, j))

s, targetx, targety = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

virus.sort()   # 작은 번호의 바이러스부터 증식
q = deque(virus)

while q:
    v, time, x, y = q.popleft()

    # 시간이 다 된 경우 break
    if time == s:
        break

    # 상하좌우에 대해 확인 -> 바이러스가 퍼질 수 있는 경우(0인 경우) 방문처리 & 큐에 추가
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < n :
            if graph[nx][ny] == 0:
                q.append((v, time+1, x, y))  # 한번 증식한 것이므로 시간 1초 추가
                graph[nx][ny] = v

print(graph[targetx-1][targety-1])

