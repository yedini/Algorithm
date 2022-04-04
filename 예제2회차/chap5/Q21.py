from collections import deque
n, l, r = map(int, input().split())

graph= []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

trans=[]  # graph 돌면서 인구 이동을 할 칸들을 저장
result = 0

while True:  # 더이상 인구이동이 발생하지 않을 때까지 반복
    flag = False  # 인구이동 여부
    visited = [[False]*n for _ in range(n)]  # 방문 여부 확인

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:  # 아직 방문 안한 곳인 경우
                queue = deque([[i, j]])
                visited[i][j] = True
                _sum = graph[i][j]  # _sum: 인구이동이 일어났을 때 인구이동에 해당하는 칸들의 합을 계산
                trans = [[i, j]]    # trans: 인구이동이 일어났을 때 해당 위치 값들을 바꾸기 위해 위치정보 저장

                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                            if l <= abs(graph[x][y] - graph[nx][ny]) <= r:   # 차이가 l 이상 r 이하인 경우 queue에 추가
                                visited[nx][ny] = True
                                queue.append([nx, ny])
                                trans.append([nx, ny])
                                _sum += graph[nx][ny]

                # 인구이동이 발생한 경우
                if len(trans) > 1:
                    flag = True
                    for x, y in trans:   # 인구이동이 늘어난 칸들의 인구수를 update
                        graph[x][y] = _sum // len(trans)

    if flag:
        result += 1
    else:
        break

print(result)