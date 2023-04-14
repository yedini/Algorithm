from collections import deque

def bfs(maps, arr, m, n, graph, xs, ys, startnum):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    q = deque()
    q.append((xs, ys, startnum))
    graph[xs][ys] = 0
    while q:
        x, y, now = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<m and 0<=ny<n and maps[nx][ny] != 'X' and graph[nx][ny] == -1:
                q.append((nx, ny, now+1))
                graph[nx][ny] = now+1
    
    return graph[arr[0]][arr[1]]

def solution(maps):
    answer = 0
    m = len(maps)
    n = len(maps[0])
    # 시작지점, 출구, 레버 찾기
    for i in range(m):
        for j in range(n):
            if maps[i][j] == 'S':
                start = [i, j]
            elif maps[i][j] == 'L':
                lever = [i,j]
            elif maps[i][j] == 'E':
                end = [i,j]
                
    # 방문 표시를 위한 graph 생성 - 레버용, 출구용 따로
    graph1 = [[-1]*n for _ in range(m)]
    graph2 = [[-1]*n for _ in range(m)]
    
    # 레버 찾는 bfs 실행
    lever_num = bfs(maps, lever, m, n, graph1, start[0], start[1], 0)

    if lever_num == -1:
        return lever_num
    else:
        return bfs(maps, end, m, n, graph2, lever[0], lever[1], lever_num)