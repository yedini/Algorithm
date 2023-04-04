from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    # 테두리는 1, 나머지는 -1로 표시한 recs와 방문여부 및 거리를 나타내는 graph 생성
    recs = [[-1]*102 for _ in range(102)]
    graph = [[-1]*102 for _ in range(102)]
    
    for i in rectangle:
        i = [j*2 for j in i]  # 모든 값을 두배로
        for j in range(i[0], i[2]+1):
            for k in range(i[1], i[3]+1):
                if i[0]<j<i[2] and i[1]<k<i[3]:  # 직사각형 내부를 모두 0으로 채움
                    recs[j][k] = 0
                elif recs[j][k] != 0:  # 다른 직사각형 내부가 아니면서 현재 직사각형의 테두리 -> 1
                    recs[j][k] = 1     
                
    # bfs
    q = deque()
    q.append((characterX*2, characterY*2, 0))
    graph[characterX*2][characterY*2] = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while q:
        x, y, dist = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<nx<=100 and 0<ny<=100 and recs[nx][ny] == 1 and graph[nx][ny] == -1:
                graph[nx][ny] = dist+1
                q.append((nx, ny, dist+1))

    # 두배 해줬으므로 2로 나눈 값이 정답
    return graph[itemX*2][itemY*2]//2