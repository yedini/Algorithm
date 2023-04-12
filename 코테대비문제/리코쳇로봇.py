from collections import deque
def solution(board):
    answer = 0
    m = len(board)
    n = len(board[0])
    graph = [[-1]*n for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'R':
                R = (i, j)
            elif board[i][j] == 'G':
                G = (i, j)
                
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append((R[0], R[1], 0))
    graph[R[0]][R[1]] = 0
    
    while q:
        x, y, now = q.popleft()
        for i in range(4):
            nx = x
            ny = y
            while 0<=nx+dx[i]<m and 0<=ny+dy[i]<n and board[nx+dx[i]][ny+dy[i]] != 'D':
                nx += dx[i]
                ny += dy[i]
            if graph[nx][ny] == -1 or graph[nx][ny]>now+1:
                q.append((nx, ny, now+1))
                graph[nx][ny] = now+1
                
    return graph[G[0]][G[1]]