n, m = map(int, input().split())  # 맵 크기

d = [[0] * m for _ in range(n)]  # 맵 생성
x, y, direction = map(int, input().split())  # 현재 캐릭터 좌표, 방향
d[x][y] = 1 # 현재 좌표는 방문한걸로 처리

# 맵 정보
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

#방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전하는 함수
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션
count = 1
turn_time = 0
while True:
    turn_left() # 왼쪽으로 회전
    nx = x + dx[direction]
    ny = y + dx[direction]

    # 회전해서 정면에 가보지 않은 칸이 있으면: 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count +=1 
        turn_time = 0
        continue

    # 회전했는데 정면이 가본 칸이거나 바다인 경우
    else:
        turn_time += 1

    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        # 뒤로 갈 수 있으면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        
        # 뒤가 바다인 경우
        else:
            break
        turn_time = 0

print(count)




