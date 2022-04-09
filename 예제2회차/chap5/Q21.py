# 하루동안 연합가능한 나라들을 파악하고, 해당 나라들에 인구이동 발생
# 이 때 하루에 일어나는 n번의 연합을 모두 묶어 한 번의 인구이동으로 본다
# 하루에 한번이라도 연합이 발생하는 경우 인구이동이 발생하므로 그 다음날도 확인해야 함.
from collections import deque
n, l, r = map(int, input().split())

graph= []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

trans=[]  # graph 돌면서 인구 이동을 할 칸들을 저장
result = 0 # 인구이동 발생 횟수

while True:  # 더이상 인구이동이 발생하지 않을 때까지 반복
    flag = False  # 하루의 인구이동 여부(연합이 한번이라도 있는지)
    visited = [[False]*n for _ in range(n)]  # 방문 여부 확인

    # 모든 위치의 나라들을 확인(모든 나라를 돌아가면서 연결되는 나라가 있는지 확인한다)
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:  # 아직 방문 안한 곳인 경우
                queue = deque([[i, j]])
                visited[i][j] = True
                _sum = graph[i][j]  # _sum: 연합이 일어났을 때 연합에 해당하는 칸들의 합을 계산
                trans = [[i, j]]    # trans: 연합이 일어날 경우 해당 위치 인구수를 바꾸기 위해 위치정보 저장

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

                # 연합이 발생한 경우
                if len(trans) > 1:
                    flag = True
                    for x, y in trans:   # 연합하는 칸들의 인구수를 update
                        graph[x][y] = _sum // len(trans)

    # 한번이라도 연합이 발생한 경우-> result가 1 증가하고 위 코드를 반복한다
    # (하루동안 여러나라 연합이 있었어도 인구이동이 한번 일어난것: 1일에 인구이동 1번으로 쳐서 result += 1)
    if flag:
        result += 1
    else:
        break

print(result)