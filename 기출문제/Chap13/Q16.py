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

# 벽을 세울 후보 빈칸들에 대한 리스트
trylist = list(combinations(empty, 3))

# 상하좌우 설정
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1] 

# 바이러스 퍼트리는 함수
def virus(x, y):
    for i in range(4): # 상하좌우로 옮겨가면서 바이러스 퍼트리기
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and ny >= 0 and nx <N and ny <M:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

# 모든 조합에 대한 계산
result = 0
for x in trylist:
    temp = copy.deepcopy(l) # 후보마다 다 계산해봐야되니까 맵 복사해오기
    for i in x:             # 후보에 속하는 세 지점에 벽 세우기
        temp[i[0]][i[1]] = 1
        
    # 바이러스 전파
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 2:  #바이러스인 지점부터 전파 시작
                virus(i, j)

    # 빈칸 세기
    score = 0 
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                score += 1
    result = max(result, score)

print(result)

