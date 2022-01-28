from itertools import combinations
import copy
N, M = map(int, input().split())

# 연구소 맵
l = []
for i in range(N):
    l.append(list(map(int, input().split())))

# 빈칸인 위치 기록
empty = []
for i in range(N):
    for j in range(M):
        if l[i][j] == 0:
            empty.append([i, j])

# 벽을 세울 후보 빈칸 리스트
trylist = list(combinations(empty, 3))

# 상하좌우
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1] 

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and ny >= 0 and nx <N and ny <M:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

result = 0
for x in trylist:
    temp = copy.deepcopy(l)
    for i in range(3):
        temp[x[i][0]][x[i][1]] = 1
        
    # 바이러스 전파
    for i in range(N):
        for j in range(M):
            if l[i][j] == 2:
                virus(i, j)

    # 빈칸 세기
    score = 0 
    for i in range(N):
        for j in range(M):
            if l[i][j] == 0:
                score += 1
    result = max(result, score)

print(temp)
print(result)

