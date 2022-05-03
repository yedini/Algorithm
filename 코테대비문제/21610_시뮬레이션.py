from collections import deque
n, m = map(int, input().split())

# 방향 순서에 맞춘 dx, dy
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

graph = [list(map(int, input().split())) for _ in range(n)]
# 비구름 위치 q에 저장
q = deque([[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]])

for u in range(m):  # m: 이동정보
    c = [[0]*n for _ in range(n)]
    d, s = map(int, input().split())  # 이동할 방향, 위치
    d -= 1 # 0부터니까 1 빼주기

    qlen = len(q)
    while qlen:
        x, y = q.popleft()
        nx = x + s*dx[d]
        ny = y + s*dy[d]

        if nx >= n:
            nx %= n  # 나머지값이 nx가 됨
        elif nx <0 :
            nx = (n-1) - (((-1)*nx - 1)%n)
        if ny >= n:
            ny %= n
        elif ny <0:
            ny = (n-1) - (((-1)*ny - 1)%n)

        q.append([nx, ny])
        qlen -=1

    for k in q:
        x, y = k
        if c[x][y] == 0:
            graph[x][y] += 1
            c[x][y] = 1
    
    q = deque([])
