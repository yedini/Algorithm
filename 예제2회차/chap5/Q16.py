# 지도 크기가 3~8, 벽 3개: 범위가 작으니까 벽 3개 세우는 모든 경우의 수를 고려해보자
# 특정 위치 값이 바이러스 일 때, 벽 내부에서 다 퍼지는 함수 필요
# 벽 세우는 모든 경우의 수에 대해 벽을 세워보고,
# 맵을 탐색하면서 바이러스면 나머지 다 터트리기
# 각 경우의 수에 대해 빈칸의 개수 세서 최대값을 출력하기
from itertools import combinations
from copy import deepcopy
n, m = map(int, input().split())

graph = []
empty=[]
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] == 0:
            empty.append([i, j])  # 뒤에서 빈칸 후보 리스트 만들기 위해 빈칸인 위치들을 저장


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 바이러스 퍼트리는 함수
def dfs(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx>=0 and nx<n and ny>=0 and ny<m and temp[nx][ny] == 0:
            temp[nx][ny] = 2
            dfs(nx, ny)

# 벽 세울 후보 리스트 뽑기

cand = list(combinations(empty, 3))

result = 0

for l in cand:
    temp = deepcopy(graph)
    for i in l:
        temp[i[0]][i[1]] = 1

    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2:
                dfs(i, j)

    # 빈칸 세기
    nums = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                nums += 1

    result = max(result, nums)

print(result)


