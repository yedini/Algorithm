n = int(input())
k = int(input())

d=[[0]*(n+1) for _ in range(n+1)]  # 맵 생성

# 사과 위치정보 -> 맵에서 사과있는 곳을 1로 표시
for _ in range(k):
    a, b = map(int, input().split())
    d[a][b] = 1

l = int(input())
# 방향 회전 정보
info = []
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

# 방향 정의: 동, 남, 서, 북(오른쪽을 보고 있음)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == "L":  #왼쪽으로 회전
        direction = (direction - 1) % 4
    else:  # 오른쪽으로 회전
        direction = (direction + 1) % 4
    return direction


def simulate():
    x, y = 1,1  # 처음 뱀의 머리위치
    d[x][y] = 2  #뱀이 있는 위치는 2로 표시
    direction = 0 # 동쪽을 가면서 시작
    time = 0
    index = 0  # 다음 회전정보
    q = [(x, y)]  # 뱀이 차지중인 위치

    while True:
        nx = x+dx[direction]
        ny = y+dy[direction]
        # 맵 상에 있고, 뱀의 몸통이 없는 위치
        if 1 <= nx and nx <= n and 1<=ny and ny<=n and d[nx][ny] !=2:
            # 사과가 없는 경우 -> 이동 후 꼬리 제거
            if d[nx][ny] == 0:
                d[nx][ny] = 2
                q.append((nx, ny))
                # 꼬리 제거
                px, py = q.pop(0)
                d[px][py] = 0
            #사과가 있는 경우 -> 이동 후 꼬리 그대로 두기
            if d[nx][ny] == 1:
                d[nx][ny] = 2
                q.append((nx, ny))
        
        # 벽이나 뱀의 몸통과 부딪힌 경우
        else:
            time += 1
            break

        # 다음 위치로 머리 이동
        x, y = nx, ny
        time += 1
        # 회전할 시간인지 확인
        if index <1 and time == info[index][0]:
            direction = turn(direction, info[index][1])
            index += 1 ## index가 의미하는게 정확히 뭐지?

    return time

print(simulate())

        

