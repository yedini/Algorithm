n, m = map(int, input().split())
x, y, direction = map(int, input().split())   # 행 위치, 열 위치, 방향

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 이동방향: 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 방문 위치 저장할 맵
visited = [[0]*m for _ in range(n)]

# 왼쪽으로 회전하는 함수
def turn_left():
    global direction
    direction -= 1  # 반시계 방향으로 90도 회전 -> 1씩 빼줌
    if direction == -1:
        direction = 3

visited[x][y] = 1  # 출발 위치를 방문처리
count = 1        # 방문 수
turn_time = 0    # 한 위치에서 회전한 수
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dx[direction]

    # 정면에 가보지 않은 칸이 존재할 경우 이동
    if visited[nx][ny] == 0 and graph[nx][ny] == 0:
        visited[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue

    else:
        turn_time += 1  # 방향 회전

    # 네 방향 모두 갈 수 없는 경우 -> 현재 방향 기준 한 칸 뒤로 가기
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있는 경우 이동
        if graph[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)
