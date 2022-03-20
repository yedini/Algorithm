n = int(input())
k = int(input())

# 보드 만들기
board = [[0]*(n+1) for _ in range(n+1)]

# 사과가 있는 곳은 1로 표시하기
for _ in range(k):
    i, j = map(int, input().split())
    board[i][j] = 1

# 회전 시간, 위치
l = int(input())

rotations = dict()   # key: 회전시간, value:위치 인 dictionary 만들기
for _ in range(l):
    t, d = input().split()
    rotations[int(t)] = d

# 방향 지정: 동, 남, 서, 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 90도 회전하는 함수: D면 오른쪽으로, L이면 왼쪽으로 회전
def rotate(d, r):
    if d == 'D':
        r += 1
    else:
        r -= 1
    
    if r > 3:
        return r-4
    elif r < 0:
        return r+4
    return r

x, y = 1, 1  # 시작 위치
board[x][y] = 2  # 뱀이 존재하는 위치
nowr = 0   # 현재 방향: 0(동쪽)에서 시작
sall = [(x,y)]  # 뱀이 차지하는 자리들
time = 0
while True:
    time += 1
    nx = x + dx[nowr]
    ny = y + dy[nowr]
    # 범위 내에 들어가 있고 뱀 몸통의 위치가 아닐 때
    if nx >= 1 and nx <= n and ny >=1 and ny <= n and board[nx][ny] != 2:
        board[nx][ny] == 2
        sall.append((nx, ny))
        # 사과가 없을 경우 -> 꼬리 없애고 이동
        if board[nx][ny] != 1:
            board[nx][ny] = 2
            # 몸길이가 1일 경우 이전 위치를 0으로 / 2 이상일 경우 가장 끝쪽 꼬리의 흔적 지우기
            ex, ey = sall.pop(0)
            board[ex][ey] = 0
    else:  # 범위 밖이거나 몸통에 부딪혔을 때
        break
    
    # 현재위치 update
    x = nx
    y = ny

    # 회전해야 될 시간일 경우 회전
    if time in rotations.keys():
        nowr = rotate(rotations[time], nowr)

print(time)


